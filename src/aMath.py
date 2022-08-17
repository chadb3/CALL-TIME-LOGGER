def compute(numerator,denominator):
    i=0
    while(numerator/(denominator+i)>=.60):
        i+=1
    print("{}/{} -> {}/{} ---- +{} = {}".format(numerator,denominator,numerator,denominator+i,i,i+denominator))
    print("\n{}/{} = {}\n\nTO {}/{} = {}".format(numerator,denominator,numerator/denominator,numerator,denominator+i,numerator/(denominator+i)))
def compute2(numerator,denominator,percentage):
    i=0
    while(numerator/(denominator+i)>=percentage/100):
        i+=1
    print("{}/{} -> {}/{} ---- +{} = {}".format(numerator,denominator,numerator,denominator+i,i,i+denominator))
    print("\n{}/{} = {}\n\nTO {}/{} = {}".format(numerator,denominator,numerator/denominator,numerator,denominator+i,numerator/(denominator+i)))

