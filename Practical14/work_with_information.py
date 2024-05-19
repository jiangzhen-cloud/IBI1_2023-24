import xml.etree.ElementTree as ET
from xml.sax import make_parser
import datetime
import matplotlib.pyplot as plt
import xml.sax

# Define the SAX API handler class
class SAX_API(xml.sax.ContentHandler):
    def __init__(self):
        self.biological_process=0
        self.molecular_function=0
        self.cellular_component=0
        self.current_element=""
        self.namespace=""
    
    def startElement(self,name,attributes):
        self.current_element=name
    
    def characters(self,content):
        if self.current_element=="namespace":
            self.namespace+=content

    def endElement(self,name):
        if self.current_element=="namespace":
            if self.namespace=="molecular_function":
                self.molecular_function+=1
            elif self.namespace=="biological_process":
                self.biological_process+=1
            elif self.namespace=="cellular_component":
                self.cellular_component+=1    
            self.current_element=""
            self.namespace=""


# Define functions for DOM parsing
def dom_parser(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    counts = {'molecular_function': 0, 'biological_process': 0, 'cellular_component': 0}
    
    for term in root.findall('term'):
        namespace = term.find('namespace').text
        if namespace in counts:
            counts[namespace] += 1
    
    return counts

# Define the main function
def main(xml_file):
    # DOM API
    start_time_dom = datetime.datetime.now()
    dom_counts = dom_parser(xml_file)
    end_time_dom = datetime.datetime.now()
    dom_duration = end_time_dom - start_time_dom
    
    # SAX API
    parser = make_parser()
    handler = SAX_API()
    start_time_sax = datetime.datetime.now()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time_sax = datetime.datetime.now()
    sax_duration = end_time_sax - start_time_sax
    
    # Print the results
    print("DOM counts:", dom_counts)
    print("SAX counts:", handler.molecular_function)
    print("SAX counts:", handler.biological_process)
    print("SAX counts:", handler.cellular_component)
    print("DOM duration:", dom_duration)
    print("SAX duration:", sax_duration)
    
    # Plotting a chart
    labels = ['Molecular Function', 'Biological Process', 'Cellular Component']
    dom_data = [dom_counts['molecular_function'], dom_counts['biological_process'], dom_counts['cellular_component']]
    sax_data = [handler.molecular_function, handler.biological_process, handler.cellular_component]
    
    plt.figure(figsize=(10, 6))
    plt.bar(labels, dom_data, label='DOM API')
    plt.bar(labels, sax_data, bottom=dom_data, label='SAX API', alpha=0.5)
    plt.legend()
    plt.title('Frequency of GO Terms in Three Ontologies')
    plt.xlabel('Ontology')
    plt.ylabel('Frequency')
    plt.show()
    
    # Record which API is the fastest
    if dom_duration < sax_duration:
        print("Comment: DOM API ran faster.")
    else:
        print("Comment: SAX API ran faster.")

if __name__ == "__main__":
    main('go_obo.xml')