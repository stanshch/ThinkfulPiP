from optparse import OptionParser

parser = OptionParser()
parser.add_option("-m", "--meal", dest="meal", help="pre-tax cost of the meal", type="float")
parser.add_option("-x", "--tax", dest="tax", help="the tax rate in the 0.XX format", type="float")
parser.add_option("-p", "--tip", dest="tip", help="your tip in the 0.XX format", type="float", default=0.20)

(options, args) = parser.parse_args()

if not (options.meal and options.tax):
	parser.error("You need to supply both the pre-tax meal and tax rate")

tax_value = options.meal*options.tax
meal_with_tax = options.meal + tax_value
tip_value = meal_with_tax*options.tip
total = meal_with_tax+tip_value

print "The base cost of the meal is $%1.2f" %options.meal
print "Your tax is $%1.2f" %tax_value
print "The tip you will pay is $%1.2f" %tip_value
print "Your grand total is $%1.2f" %total