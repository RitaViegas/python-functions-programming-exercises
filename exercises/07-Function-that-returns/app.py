def dollar_to_euro(dollar_value):
	return dollar_value * 0.91

def euro_to_yen(euro_value):
	return euro_value * 161.70

####### ↓ YOUR CODE BELOW ↓ #######
resultado_1 = dollar_to_euro(137)
resultado_2_euro_para_yen = euro_to_yen(resultado_1)
print(resultado_2_euro_para_yen)