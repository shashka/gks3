import line

def main():
	start, end = [(20, 25), (40, 85)]
	angle = 71
	line1 = line.LinePath(start, end, angle)
	line1.get_endpoint_by_angle()
	line1.get_line_func()
	line1.calc_parametr(T=3, V=5, step=5, plotted=True)
	line1.get_path_by_interpolation_predict(5, True)
	line1.method_cont_carrier_freq(True)
	line1.CDA(True)

if __name__ == "__main__":
	main()
