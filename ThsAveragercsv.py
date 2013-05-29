import sys
class ThsAverager:
  def __init__(self, input_file, output_file, ndata, init_temp, final_temp):
		self.input_file = input_file
		self.output_file = output_file
		self.ndata = ndata
		self.init_temp = init_temp
		self.final_temp = final_temp

	def Average_Calculate(self):
		count = 1
		sum = []
		ip = open(self.input_file, "r")
		op = open(self.output_file, "a")
		a = ip.readline()
		op.write(a)
		op.write("\n")
		while True:
        		for i in range(0, self.ndata+1):
                		sum.insert(i, 0.0)
        		a = ip.readline().strip().split(",")
        		for i in range(0, self.ndata+1):
                		sum[i] = sum[i] + float(a[i])
        		while True:
                		a1 = ip.readline().strip().split(",")
                		if float(a1[0]) == float(a[0]):
                        		for i in range(0, self.ndata+1):
                                		sum[i] = sum[i] + float(a1[i])
                        		count = count +1
                		else:
                        		for i in range(0, self.ndata+1):
                                		op.write(str.format("%5.2f" %(sum[i]/count) + ","))
                        		op.write("\n")
                        		sum = []
                        		for i in range(0, self.ndata+1):
                               			sum.insert(i, 0.0)
                        		for i in range(0, self.ndata+1):
                                		sum[i] = sum[i] + float(a1[i])
                        		count = 1
                        		self.init_temp = self.init_temp + 1
                        		break
        		if self.init_temp >= self.final_temp:
                		break
		ip.close()
		op.close()
