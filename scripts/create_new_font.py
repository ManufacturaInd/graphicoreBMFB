#!/usr/bin/env python
import jinja2
import click
import sys, os

TEMPLATE_PATH = './jsn-templates'

@click.command()
@click.option("-f", "--font-name", prompt='Font/Family name')
@click.option("-n", "--designer-name", prompt='Designer name')
@click.option("-u", "--designer-url", prompt='Designer URL')
@click.option("-m", "--manufacturer-name", prompt='Manufacturer name')
@click.option("-v", "--vendor-url", prompt='Vendor URL')
@click.option("-d", "--description", prompt='Description (1 paragraph max)')
@click.option("-t", "--trademark", prompt='Trademark notice')
def generate_font(font_name, designer_name, designer_url, manufacturer_name, vendor_url, description, trademark):
    context = { "font_name" : font_name,
                "file_name" : font_name.replace(' ', ''),
                "designer_name": designer_name,
                "designer_url": designer_url,
                "manufacturer_name": manufacturer_name,
                "vendor_url": vendor_url,
                "description": description + " Built with graphicoreBMFB and Fontforge.",
                "trademark_notice": trademark,
                }

    output_dir = context["file_name"]
    if os.path.exists(output_dir):
        print "Directory %s exists, not going on."
        sys.exit()
    os.mkdir(output_dir)

    loader = jinja2.FileSystemLoader(searchpath=TEMPLATE_PATH)
    env = jinja2.Environment(loader=loader)

    for t in os.listdir(TEMPLATE_PATH):
        template = env.get_template(t)
        output = template.render(context)
        filename = os.path.join(output_dir, t.replace('BitmapFont', context['file_name'] + '-'))
        f = open(filename, 'w')
        f.write(output)
        f.close()

    print "Done! The license was automatically set to the Open Font License (OFL)."

if __name__ == "__main__":
    generate_font()
