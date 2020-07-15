#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from arcor2.services.upload import upload


def main():

    upload("arcor2_kinali.services.robot/RestRobotService")
    upload("arcor2_kinali.services.search/SearchService")
    upload("arcor2_kinali.services.barcode/BarcodeService")
    upload("arcor2_kinali.services.statistic/StatisticService")
    upload("arcor2_kinali.services.interaction/InteractionService")


if __name__ == "__main__":
    main()
