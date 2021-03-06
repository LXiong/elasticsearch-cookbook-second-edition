import elasticsearch
from pprint import pprint

es = elasticsearch.Elasticsearch()
index_name = "my_index"
type_name = "my_type"

from utils import create_and_add_mapping, populate

create_and_add_mapping(es, index_name, type_name)
populate(es, index_name, type_name)

results = es.search(index_name, type_name,
                    {
                        "query": {"match_all": {}},
                        "aggs": {
                            "pterms": {"terms": {"field": "parsedtext", "size": 10}}
                        }
                    })
pprint(results)

results = es.search(index_name, type_name,
                    {
                        "query": {"match_all": {}},
                        "aggs": {
                            "date_histo": {"date_histogram": {"field": "date", "interval": "month"}}
                        }
                    })
pprint(results)

es.indices.delete(index_name)
