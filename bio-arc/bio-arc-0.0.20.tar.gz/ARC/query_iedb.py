"""
File to query + download the receptor data from the IEDB
"""
import os
import pymysql as mdb
import pandas as pd

def run_sql(sql_command, filename):
    try:                 
        connection = mdb.connect(host='iedb-mysql.liai.org',
        port= 33306, 
        user= 'acrinklaw',
        passwd= '',
        db='iedb_curation',
        charset='utf8'
        )
    except (mdb.OperationalError, mdb.ProgrammingError) as msg:
        raise Exception(msg)
    except mdb.InternalError as msg:
        raise Exception(msg)

    cursor = connection.cursor()
    cursor.execute(sql_command)
    header = [i[0] for i in cursor.description]
    header=list(header)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    print ('Number of proteins in IEDB: '+str(cursor.rowcount))
    inp = pd.DataFrame(list(result), columns=header)
    inp.to_csv(filename, index=False, encoding="utf-8")
    
    return inp

def get_IEDB_receptors():
    protein_sql = """SELECT s.* FROM iedb_curation.source s, iedb_curation.epitope e, iedb_curation.object o WHERE e.e_object_id = o.object_id AND o.mol2_source_id = s.source_id AND s.chemical_type=\'Protein\'"""
    protein_file = os.path.join(os.path.dirname(__file__),'./iedb_proteins.tsv')
    protein_df=run_sql(protein_sql, protein_file)
    
    return protein_df

get_IEDB_receptors()