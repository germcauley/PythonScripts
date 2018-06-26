from PIL import Image, ImageDraw
from selenium import webdriver
import os
import sys

class ScreenAnalysis:

    # STAGING_URL = 'https://www.google.ie/search?hl=en&dcr=0&source=hp&ei=2xQMWoH0JaSQgAb1vrvIBw&q=cars&oq=cars&gs_l=psy-ab.3..35i39k1j0i20i263k1j0j0i20i263k1j0l6.1417.1847.0.2439.5.4.0.0.0.0.111.404.2j2.4.0....0...1.1.64.psy-ab..1.4.402.0..0i131k1j0i131i46k1j46i131k1.0.lZeMddIUQns'
    # PRODUCTION_URL = 'https://www.google.ie/search?hl=en&dcr=0&ei=3hQMWsznI-SCgAbYwovoBQ&q=cats&oq=cats&gs_l=psy-ab.3..0i67k1l4j0l6.6010.6458.0.7047.4.4.0.0.0.0.152.477.1j3.4.0....0...1.1.64.psy-ab..0.4.474...35i39k1j0i131k1.0.6dlA8dsdeDw'
    # #STAGING_URL = "https://help-centre.zone-dev1.aws/cludo-search-results/"
    #PRODUCTION_URL = "https://help-centre.zone-dev1.aws/cludo-search-results/#?cludoquery=cards&cludopage=1"
    driver = None

    def __init__(self, path1, path2):
        self.set_up()
        # self.capture_screens()
        self.path1 = path1
        self.path2 = path2
        self.analyze()
        self.clean_up()

    def set_up(self):
        self.driver = webdriver.PhantomJS()

    def clean_up(self):
        self.driver.close()

    # def capture_screens(self):
        # self.STAGING_URL = self.url1
        # self.PRODUCTION_URL = self.url2
        # self.screenshot(self.STAGING_URL, 'screen_staging.png')
        # self.screenshot(self.PRODUCTION_URL, 'screen_production.png')

    def screenshot(self, url, file_name):
        print("Capturing", url, "screenshot as", file_name, "...")
        self.driver.get(url)
        self.driver.set_window_size(1024, 768)
        self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'screenshots', file_name))
        self.driver.get_screenshot_as_png()
        print("Done.")

    def analyze(self):
        # screenshot_staging = Image.open("screenshots/screen_staging.png")
        # screenshot_production = Image.open("screenshots/screen_production.png")
        # screenshot_staging = Image.open("/Users/gmcauley/PycharmProjects/PageObjectModelExample/venv/screenshots/ProductsImage2.png")
        # screenshot_production = Image.open("/Users/gmcauley/PycharmProjects/PageObjectModelExample/venv/screenshots/ProductsImage3.png")
        #
        screenshot_staging = Image.open(self.path1)
        screenshot_production = Image.open(self.path2)
        columns = 60
        rows = 80
        screen_width, screen_height = screenshot_staging.size

        block_width = ((screen_width - 1) // columns) + 1 # this is just a division ceiling
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                region_staging = self.process_region(screenshot_staging, x, y, block_width, block_height)
                region_production = self.process_region(screenshot_production, x, y, block_width, block_height)

                if region_staging is not None and region_production is not None and region_production != region_staging:
                    draw = ImageDraw.Draw(screenshot_staging)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")

        screenshot_staging.save("result.png")

    def process_region(self, image, x, y, width, height):
        region_total = 0

        # This can be used as the sensitivity factor, the larger it is the less sensitive the comparison
        factor = 70

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor

