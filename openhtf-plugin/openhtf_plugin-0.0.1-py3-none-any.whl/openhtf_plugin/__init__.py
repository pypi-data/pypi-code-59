
from openhtf.output.callbacks import json_factory


from tcms_api.plugin_helpers import Backend
import os, logging


def kiwi_report_callback(test_record):
    
    backend = Backend(prefix='[OPENHTF] ')
    backend.configure()
    dut = { 'dut_id': 'None'}
    record_dict = json_factory.OutputToJSON(sort_keys = True).convert_to_dict(test_record)
    phase_no = 0
    test_execution_id = None
    dut['dut_id'] = record_dict['dut_id']
    for phase in record_dict['phases']:
         
          
        phase_no += 1
        case_name = 'phase ' + str(phase_no) +'_'+ str(phase['name'])
        test_case, _ = backend.test_case_get_or_create(case_name)
        test_case_id = test_case['id']
        
        backend.add_test_case_to_plan(test_case_id, backend.plan_id)
        test_execution_id = backend.add_test_case_to_run(
                test_case_id,
                backend.run_id)
        comment = str(dut) + ',' + str(phase['measurements'])
        
        if phase['outcome'] == 'PASS':
            status_id = backend.get_status_id('PASSED')
        elif phase['outcome'] == 'ERROR':
            status_id = backend.get_status_id('ERROR')
        else:
            status_id = backend.get_status_id('FAILED')
        backend.update_test_execution(test_execution_id,
                                               status_id,
                                               comment)
    backend.finish_test_run()
    




