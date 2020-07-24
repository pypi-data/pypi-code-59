import os
import sys

import psutil

from monk.gluon_prototype import prototype
from monk.compare_prototype import compare
from monk.pip_unit_tests.gluon.common import print_start
from monk.pip_unit_tests.gluon.common import print_status

import mxnet as mx
import numpy as np
from monk.gluon.losses.return_loss import load_loss


def test_loss_squared_hinge(system_dict):
    forward = True;
    if(not os.path.isdir("datasets")):
        os.system("! wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1rG-U1mS8hDU7_wM56a1kc-li_zHLtbq2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1rG-U1mS8hDU7_wM56a1kc-li_zHLtbq2\" -O datasets.zip && rm -rf /tmp/cookies.txt")
        os.system("! unzip -qq dataset.zip")

    test = "test_loss_squared_hinge";
    system_dict["total_tests"] += 1;
    print_start(test, system_dict["total_tests"])
    if(forward):
        try:
            gtf = prototype(verbose=0);
            gtf.Prototype("sample-project-1", "sample-experiment-1");

            label = np.random.rand(1, 5);
            label = mx.nd.array(label);

            y = np.random.rand(1, 5);
            y = mx.nd.array(y);

            gtf.loss_squared_hinge();
            load_loss(gtf.system_dict);
            loss_obj = gtf.system_dict["local"]["criterion"];
            loss_val = loss_obj(y, label);           

            system_dict["successful_tests"] += 1;
            print_status("Pass");

        except Exception as e:
            system_dict["failed_tests_exceptions"].append(e);
            system_dict["failed_tests_lists"].append(test);
            forward = False;
            print_status("Fail");
    else:
        system_dict["skipped_tests_lists"].append(test);
        print_status("Skipped");

    return system_dict
