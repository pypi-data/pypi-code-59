"""
    Utilities Package for Pyppet
"""
# __author__ = DanEdens
# __status__  = "production"

import os

from sitecheck.scanner import ROOT_DIR


def get_date() -> str:
    import datetime
    today = datetime.datetime.utcnow()
    return str(today.strftime("%Y-%m-%d"))


def make_logger() -> object:
    import logging
    log_format: str = '%(asctime)-15s - %(message)s'
    logging.basicConfig(level=None, format=log_format)
    logger = logging.getLogger(__name__.split('.')[0])
    # if options.Debug:
    #     logger.setLevel(logging.DEBUG)
    # elif options.Verbose:
    logger.setLevel(logging.INFO)
    return logger


async def wait_type(page, selector, txt):
    """
        Wait for a selector to load than type supplied text.
        Returns page in case entering text changes the context.
    """
    await page.waitForSelector(selector)
    await page.type(selector, txt)
    return page


async def wait_click(page, selector):
    """
        Wait for a selector to load than clicks on it.
        Returns page in case this changes the context.
    """
    await page.waitForSelector(selector),
    await page.click(selector)
    return page


async def wait_hover(page, selector):
    """
        Wait for a selector to load than hover over it.
        Returns page in case this changes the context.
    """
    await page.waitForSelector(selector),
    await page.hover(selector)
    return page


async def screenshot(self, sensor, name_sel):
    project_images = ROOT_DIR+'\\Screenshots\\'+self.project.name+'\\'
    if os.path.exists(project_images):
        pass
    else:
        os.makedirs(project_images)
    await wait_hover(self.page, name_sel)
    await self.page.waitFor(500)
    await self.page.screenshot({'path': project_images+sensor+'_'+get_date()+'.png'})


def disable_timeout_pyppeteer():
    """
        Allows Browser to be left open indefinitely
        Keeps Session open longer than 20 seconds.

        :return:
    """
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    pyppeteer.connection.websockets.client.connect = new_method
