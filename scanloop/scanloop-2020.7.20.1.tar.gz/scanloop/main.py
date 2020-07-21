#!/usr/bin/python3

"""A scanner front-end to efficiently scan several multi-page documents."""

import argparse
import logging
import os
import re
import subprocess
import sys
import time


try:
    from .version import __version__
except Exception as ex:
    logging.error("unable to determine version: %s", ex)
    __version__ = "unknown"


def command_exists(command):
    """Returns true if the given command is available in the system."""
    return subprocess.call(["which", command]) == 0


class ScanLoop(object):
    """Scans documents in a loop."""

    def __init__(self, quality_percent, scan_cmd,
                 scan_format, output_format, pdf_viewer):
        self.quality_percent = quality_percent
        self.scan_command = (scan_cmd or ScanLoop.guess_scan_command()).split()
        self.pdf_viewer = pdf_viewer # allow setting no pdf viewer
        self.scan_format = scan_format
        self.output_format = output_format


    @staticmethod
    def guess_scan_command():
        """Attempts to guess the scan command."""
        env_cmd = os.getenv("SCAN_CMD")
        if env_cmd:
            return env_cmd
        logging.info("checking scanner availability via scanimage...")
        if command_exists("imagescan"):
            return "{} {}".format("imagescan", " --no-interface")
        if command_exists("scanimage") and subprocess.call(
                ["sudo", "scanimage", "-L"]) == 0:
            return "sudo scanimage"
        return None


    @staticmethod
    def guess_pdf_viewer():
        """Attempts to guess the scan command."""
        for pdf_viewer in ("zathura", "evince", "gv", "open"):
            if command_exists(pdf_viewer):
                return pdf_viewer
        logging.warn("no pdf viewer could be guessed")
        return None


    def check_requirements(self):
        """Check all requirements are satisfied before scanning."""
        if not command_exists("convert"):
            raise Exception(
                "missing imagemagic convert. hint: {apt-get,brew} install imagemagick")
        if not self.scan_command:
            raise Exception("no scan command detected")


    def list_ordered_pages(self, extension=None):
        """Lists pages in the cwd as a two-tuple: (page_num, page_fname)."""
        if not extension:
            extension = self.scan_format
        return sorted(
            (int(fname.split(".")[0]), fname)
            for fname in os.listdir(os.getcwd())
            if re.match("[0-9]+.{}".format(extension), fname))


    def scan_page(self, fname_output):
        """Scan a single page to the given output filename."""
        logging.info("scanning page to %s. Ctrl+C to stop...", fname_output)
        attempts = 0
        try:
            while True:
                attempts += 1
                with open(fname_output, "wb") as fh:
                    p = subprocess.Popen(self.scan_command,
                                         stdout=fh,
                                         stderr=subprocess.PIPE)
                # print ("DEBUG TRACE: scan-loop-docs 6vzg ")
                p.wait()
                # print ("DEBUG TRACE: scan-loop-docs ikow ")
                if p.returncode == 0:
                    logging.info("successfully scanned %s", fname_output)
                    return True
                _, stderr = p.communicate()
                sys.stdout.write("\rscan attempt {}. Ctr+C to stop...".format(
                    attempts))
                sys.stdout.write(" " + stderr.decode().replace("\n", " "))
                sys.stdout.flush()

                time.sleep(1)
        except KeyboardInterrupt:
            try:
                os.remove(fname_output)
            except FileNotFoundError:
                pass
            return False


    def merge_pages(self, output):
        """Merge multiple page scans into a single output file."""
        for (_, pnm) in self.list_ordered_pages(extension=self.scan_format):
            # need itermediate jpg conversion to enforce "-quality" space savings
            jpg = "{}.jpg".format(pnm.split(".")[0])
            cmd = ["convert", pnm, "-quality", str(self.quality_percent), jpg]
            ret = subprocess.call(cmd)
            if ret != 0:
                raise Exception("non-zero exit status: {} of {}".format(
                    ret, " ".join(cmd)))

        cmd = (["convert"] +
               [fname for (_, fname) in self.list_ordered_pages(extension="jpg")] +
               [output])
        logging.info("convert command: %s", " ".join(cmd))
        ret = subprocess.call(cmd)
        if ret != 0:
            raise Exception("non-zero exit status: {} of {}".format(
                ret, " ".join(cmd)))
        if self.pdf_viewer:
            subprocess.call([self.pdf_viewer, output])

    def scan_doc(self, doc_name):
        """Create a scan of a doc containing one or more pages."""
        pages = self.list_ordered_pages()
        page_no = pages[-1][0] + 1 if pages else 1
        while True:
            page = "{}.{}".format(page_no, self.scan_format)
            expect_more_pages = self.scan_page(page)
            if expect_more_pages:
                page_no += 1
            else:
                break
        if not self.list_ordered_pages():
            logging.error("no pages scanned.")
            return
        output = "{}.{}".format(doc_name, self.output_format)
        self.merge_pages(output)
        logging.info("successfully merged pages to %s", output)

    def start(self):
        """Scan documents indefinitely."""
        orig_dir = os.getcwd()
        while True:
            os.chdir(orig_dir)
            doc_name = input("enter new doc name, q to quit: ")
            if doc_name == "q":
                break
            assert "/" not in doc_name, "invalid filename"
            try:
                os.mkdir(doc_name)
            except FileExistsError:
                pass
            os.chdir(doc_name)
            self.scan_doc(doc_name)

def main():
    """Main."""
    logging.root.setLevel(logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument("--quality-percent",
                        help="The imagemagick -quality of merged document.",
                        default=30)
    parser.add_argument("--scan-cmd",
                        help="command used to scan a single page to stdout.")
    parser.add_argument("--scan-format", default="pnm",
                        help="The file-format extension of the scan command output.")
    parser.add_argument("--output-format", default="pdf",
                        help="The file-format extension of the merged document.")
    parser.add_argument("--pdf-viewer", help="Command to open the output files.",
                        default=ScanLoop.guess_pdf_viewer())
    parser.add_argument("--version", action="version", version=__version__)


    args = vars(parser.parse_args())

    logging.info("version: %s", __version__)

    scan_loop = ScanLoop(**args)
    scan_loop.check_requirements()
    scan_loop.start()

if __name__ == "__main__":
    main()
