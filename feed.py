import yaml
import xml.etree.ElementTree as xml_tree

# Open the YAML file
with open('feed.yaml', 'r') as file:
    # Load the YAML data
    yaml_data = yaml.safe_load(file)

    # Create the root 'rss' element with necessary namespaces
    rss_element = xml_tree.Element('rss', {
        'version': '2.0', 
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd', 
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    })

    # Create the 'channel' element under 'rss'
    channel_element = xml_tree.SubElement(rss_element, 'channel')

    # Set the title from YAML data
    xml_tree.SubElement(channel_element, 'title').text = yaml_data['title']

    # Generate the XML tree
    output_tree = xml_tree.ElementTree(rss_element)

# Write the XML to file after closing the YAML file
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)