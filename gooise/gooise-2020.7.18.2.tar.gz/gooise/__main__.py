def main():
    from sys import exit

    def get_arguments():
        from argparse import ArgumentParser

        def max_images(argument):
            try:
                value = int(argument)
                if value < 0:
                    raise ValueError()
                return value
            except ValueError:
                from argparse import ArgumentTypeError
                raise ArgumentTypeError("maximum amount of images is expected to be an unsigned integer number")

        parser = ArgumentParser(prog="gooise", description="Google Image Search")
        parser.add_argument("image", type=str, help="path to/url of image to lookup")
        parser.add_argument("-m", "--limit-results", type=max_images, help="maximum amount of images to fetch")

        driver_arguments = parser.add_argument_group(title="Driver parameters")
        driver_arguments.add_argument("-d", "--driver",
                                      choices=("chrome", "firefox", "opera", "ie", "edge"),
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
            if arguments.driver is None:
                browser = driver.get_any(arguments.headless)
                if not browser:
                    print("No supported web drivers installed")
                    return 2
            else:
                browser = driver.get_driver(arguments.driver, arguments.browser_binary, arguments.headless)
        except Exception:
            print("Unable to create an instance of web driver")
            return 2

        try:
            flow.get_results_page(browser, arguments.image)
            print("Related search query: " + repr(flow.fetch_related_query(browser)))
            flow.open_images_tab(browser)

            print("Loading all items before proceeding...")
            items = flow.scroll_results_list(browser, arguments.limit_results)

            if len(items) == 1:
                print("Fetching " + str(len(items)) + " URL...")
            else:
                print("Fetching " + str(len(items)) + " URLs...")
            index_pad = int(log10(len(items))) + 1
            for index, item in enumerate(items):
                first = index == 0

                try:
                    full_image = flow.open_full_image(browser, item, first)
                    flow.preload_full_image(browser, full_image, first, 3)
                except TimeoutException:
                    print(str(index + 1).rjust(index_pad, " ") + ".", "Preloading timed out")
                    continue
                flow.hover_full_image(browser, full_image)
                print(str(index + 1).rjust(index_pad, " ") + ".",
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
