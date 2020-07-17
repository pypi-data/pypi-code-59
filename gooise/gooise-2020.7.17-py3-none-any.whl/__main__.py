def main():
    from sys import exit

    def get_arguments():
        from argparse import ArgumentParser

        parser = ArgumentParser(prog="gooise", description="Google Image Search")
        parser.add_argument("image", type=str, help="path to/url of image to lookup")
        parser.add_argument("-m", "--limit-results", type=int, help="maximum amount of images to fetch")

        driver_arguments = parser.add_argument_group(title="Driver parameters")
        driver_arguments.add_argument("-d", "--driver",
                                      choices=("chrome", "firefox", "opera", "ie", "edge"),
                                      default="chrome",
                                      help="browser driver to use")
        driver_arguments.add_argument("-e", "--headless", action="store_true", help="run driver in headless mode")
        driver_arguments.add_argument("-b", "--browser-binary", type=str, help="path to browser binary location")
        return parser.parse_args()

    def run(arguments):
        from gooise.exception import BrokenFlowError, NoResultsError
        from selenium.common.exceptions import TimeoutException
        from gooise import flow, driver
        from math import log10

        # noinspection PyBroadException
        try:
            browser = driver.get_driver(arguments.driver, arguments.browser_binary, arguments.headless)
        except Exception:
            print("Unable to create an instance of web driver")
            return 2

        try:
            flow.get_results_page(browser, arguments.image)
            print("Related search query: " + repr(flow.fetch_related_query(browser)))
            flow.open_images_tab(browser)
            items = flow.scroll_results_list(browser, arguments.limit_results)
            for index, item in enumerate(items):
                first = index == 0

                try:
                    full_image = flow.open_full_image(browser, item, first)
                    flow.preload_full_image(browser, full_image, first, 3)
                except TimeoutException:
                    print(str(index + 1).ljust(int(log10(len(items))), " ") + ".", "Preloading timed out")
                    continue
                flow.hover_full_image(browser, full_image)
                print(str(index + 1).ljust(int(log10(len(items))), " ") + ".",
                      flow.get_full_image_url(full_image), "(" + flow.fetch_full_image_size(browser, first) + ")")
        except NoResultsError:
            print("Search complete - no similar images found.")
            return 0
        except BrokenFlowError as e:
            print("Unable to perform image search: " + str(e))
            print("This is quite possibly caused by search frontend updates.")
            return 3
        except KeyboardInterrupt:
            print("Stopped.")
        finally:
            browser.quit()

    exit(run(get_arguments()))


if __name__ == '__main__':
    main()
