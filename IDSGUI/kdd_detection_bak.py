
import pandas
from time import time
from collections import Counter
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans



class ids():
	def __init__(self):
		self.n_cluster=20
		self.km=KMeans(self.n_cluster)

		# Labels for the datset objects
		self.column_name = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land",
					   "wrong_fragment", "urgent", "hot", "num_failed_logins",
					   "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
					   "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
					   "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
					   "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
					   "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
					   "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
					   "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
					   "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "temp"]
		#columns with numeric features
		self.num_features = [
			"duration", "src_bytes",
			"dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
			"logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
			"num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
			"is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
			"srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
			"diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
			"dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
			"dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
			"dst_host_rerror_rate", "dst_host_srv_rerror_rate"]

		self.num_features_2 = [
			"duration","src_bytes",
			"dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins",
			"logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
			"num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
			"is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
			"srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
			"diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
			"dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
			"dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
			"dst_host_rerror_rate", "dst_host_srv_rerror_rate"]

		self.label_cluster = []
		self.kdd_train_dataset = pandas.read_csv("./dataset/unlabeled_duration.txt", header=None, names=self.column_name)
		self.kdd_test_dataset = pandas.read_csv("./dataset/unlabeled_duration(test).txt", header=None, names=self.column_name)
		self.teststd=0

	def pre_process(self, dataset):


		#Applying a scaling transformation that assigns the value between 0 and 1
		try:
			features = dataset[self.num_features].astype(float)
			kdd_minmax_scale = MinMaxScaler().fit(features[self.num_features])
			kdd_scaled = kdd_minmax_scale.transform(features[self.num_features])
		except:
			message="Please choose the correct dataset"
			return message

		# Conversion of Arrays to CSV colums
		i = 0
		for label in self.num_features:
			features[label] = kdd_scaled[:, i]
			i += 1

		return features

	def train(self, dataset):


		dataset=self.pre_process(dataset)
		pca = PCA(n_components=10)
		data = pca.fit_transform(dataset)
		print(data)
		# del data['duration']
		# for label in self.num_features_2:
		# 	del dataset[label]



		print("_____________________________________________",type(data))
		print(data)
		t0 = time()
		self.km.fit(data)
		# print(dataset['label'].value_counts())
		tt = time() - t0
		print("Clustered in {} seconds".format(round(tt, 3)))

	def predict(self, kdd_test_dataset):


		# del kdd_test_dataset['duration']
		test_set=self.pre_process(kdd_test_dataset)
		# for label in self.num_features_2:
		# 	del test_set[label]

		pca = PCA(n_components=10)
		try:
			test_data = pca.fit_transform(test_set)
		except:
			message = "Please choose the correct dataset"
			return message
        #10 bajae holaa ki
		t0 = time()
		pred = self.km.predict(test_data)
		tt = time() - t0
		print("Assigned cluster in {} seconds.".format(round(tt, 3)))
		print(pred)

		# Determination of TP, FP




		res = Counter(pred)
		print("The results are:     ",res)
		normal = 0
		neptune = 0
		smurf = 0
		back = 0
		teardrop = 0
		pod = 0
		land = 0
		anomaly=0

		for val in res:
			print(self.label_cluster[val], res[val])
			if self.label_cluster[val] == 'normal':
				normal += res[val]
			elif self.label_cluster[val] == 'neptune':
				neptune += res[val]
			elif self.label_cluster[val] == 'smurf':
				smurf += res[val]
			elif self.label_cluster[val] == 'back':
				back += res[val]
			elif self.label_cluster[val] == 'teardrop':
				teardrop += res[val]
			elif self.label_cluster[val] == 'pod':
				pod += res[val]
			elif self.label_cluster[val] == 'land':
				land += res[val]
			else:
				anomaly+=res[val]

		file=open('./file/test.txt','w')
		for i, j in zip(pred, kdd_test_dataset['label']):
			file.write(str(j)+ ","+ self.label_cluster[i] + "\n")
		file.close()

		col=['std_label','res_label']
		acc=pandas.read_csv('./file/test.txt', header=None, names=col)
		tot_normal=0
		acc_normal=0
		acc_smurf=0
		acc_neptune=0
		acc_back=0
		acc_teardrop=0
		acc_pod=0
		acc_land=0
		acc_anomaly=0

		for i, j in zip(acc['std_label'], acc['res_label']):
			print(i, j)
			if j=='normal':
				tot_normal+=1
				if i=='normal':
					acc_normal+=1
				elif i=='smurf':
					acc_smurf+=1
				elif i=='neptune':
					acc_neptune+=1
				elif i == 'back':
					acc_back +=1
				elif i == 'teardrop':
					acc_teardrop += 1
				elif i == 'pod':
					acc_pod +=1
				elif i == 'land':
					acc_land += 1
				else:
					acc_anomaly +=1


		print("For a normal value there are: ")
		print("Normal: ",acc_normal)
		print("Smurf: ",acc_smurf)
		print("Neptune: ", acc_neptune)
		print("Back: ",acc_back)
		print("Teardrop: ",acc_teardrop)
		print("POD: ",acc_pod)
		print("Land: ",acc_land)
		print("std_value")
		print(acc['std_label'].value_counts())
		print("Total value: ",tot_normal)



		# print(kdd_test_dataset['labels'].value_counts())




		print()
		print()
		print("_____________________RESULT____________________")
		print("Normal: ", normal)
		print("Neptune: ", neptune)
		print("Smurf: ", smurf)
		print("back: ", back)
		print("teardrop: ", teardrop)
		print("pod: ", pod)
		print("land: ", land)
		print("anomaly: ", anomaly)
		print("______________________________")


		count = 0
		norTP = 0
		norFN = 0
		nepTP = 0
		nepFN = 0
		smuTP = 0
		smuFN = 0

		for i in pred:
			if self.kddstd.values[:, [41]][count] == 'normal':
				if self.label_cluster[i] == 'normal':
					norTP += 1
				else:
					norFN += 1

			# print (kdd_test_dataset.values[:, [41]][count],"-",label_cluster[i])
			# print("loading...")

			elif kdd_test_dataset.values[:, [41]][count] == 'neptune':
				if self.label_cluster[i] == 'neptune':
					nepTP += 1
				else:
					nepFN += 1

			elif kdd_test_dataset.values[:, [41]][count] == 'smurf':
				if self.label_cluster[i] == 'smurf':
					smuTP += 1
				else:
					smuFN += 1

			count += 1
			print("loading...")

		print(norTP, norFN)
		print(nepTP, nepFN)
		print(smuTP, smuFN)
		print("--------------------------------------")

		rate = open("rate", "w")
		rate.write(str(norTP) + '\n')
		rate.write(str(norFN) + '\n')
		rate.write(str(nepTP) + '\n')
		rate.write(str(nepFN) + '\n')
		rate.write(str(smuTP) + '\n')
		rate.write(str(smuFN) + '\n')
		rate.close()


		file=open('./file/result.txt', 'w')
		file.writelines(str(normal)+'\n')
		file.writelines(str(neptune)+'\n')
		file.writelines(str(smurf)+'\n')
		file.write(str(back)+'\n')
		file.write(str(teardrop)+'\n')
		file.write(str(pod)+'\n')
		file.write(str(land)+'\n')
		file.writelines(str(anomaly))
		file.close()
		# print(kdd_test_dataset['label'].value_counts())

    # hait k bhanxaa yaslae...
    #clz nai aauxas ki?
    # ah chadai hidnae ho aajaa


	def assign_cluster_label(self, kdd_dataset):
		labels = kdd_dataset['label']
		label_names = list(
			map(lambda x: pandas.series([labels[i] for i in range(len(self.km.labels_)) if self.km.labels_[i] == x]), range(self.n_cluster)))

		# val = ','.join(map(str, label_names))
		for i in range(self.n_cluster):
			print("cluster {} labels: ".format(i))
			print(label_names[i].value_counts())
			label_dict = label_names[i].value_counts().to_dict()
			val = max(label_dict, key=label_dict.get)
			print(type(val))
			self.label_cluster.append(val)
			print("cluster of : ", val)



	def main(self, traindir, testdir, teststd):
				# Labels for the datset objects

			try:
				kdd_dataset = pandas.read_csv(traindir, header=None, names=self.column_name)
			except:
				message="Error has Occured. Dataset cannot be read. Please select the proper dataset."
				return message
			#pre-processing a dataset
			try:
				processed_dataset=self.pre_process(kdd_dataset)
				self.train(processed_dataset)
				self.assign_cluster_label(kdd_dataset)
			except:
				message="Please choose the correct dataset."
				return message

			try:
				kdd_test_dataset = pandas.read_csv(testdir, header=None, names=self.column_name)
			except:
				message="Test dataset cannot be read."
				return message

			pred = self.predict(kdd_test_dataset)

			column_name_label = ["protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land",
							   "wrong_fragment", "urgent", "hot", "num_failed_logins",
							   "logged_in", "num_compromised", "root_shell", "su_attempted", "num_root",
							   "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
							   "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate",
							   "srv_serror_rate", "rerror_rate", "srv_rerror_rate", "same_srv_rate",
							   "diff_srv_rate", "srv_diff_host_rate", "dst_host_count", "dst_host_srv_count",
							   "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate",
							   "dst_host_srv_diff_host_rate", "dst_host_serror_rate", "dst_host_srv_serror_rate",
							   "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label", "temp"]
			for label in column_name_label:
				del kdd_test_dataset[label]
				del kdd_dataset[label]

			try:
				kdd_test_std = pandas.read_csv(teststd, header=None, names=self.column_name)
			except:
				message = "Standard Test dataset cannot be read."
				return message
			normal = 0
			neptune = 0
			smurf = 0
			back = 0
			teardrop = 0
			pod = 0
			land = 0
			anomaly=0

			list=kdd_test_std['label'].value_counts().to_dict()
			print(kdd_test_std['label'].value_counts())
			for key in list.keys():
				if key=='normal':
					normal=list[key]
				elif key=='neptune':
					neptune=list[key]
				elif key == 'smurf':
					smurf = list[key]
				elif key == 'back':
					back = list[key]
				elif key == 'teardrop':
					teardrop = list[key]
				elif key == 'pod':
					pod = list[key]
				elif key == 'land':
					land = list[key]
				else:
					anomaly=list[key]


			file=open('./file/std.txt', 'w')
			file.writelines(str(normal) + '\n')
			file.writelines(str(neptune) + '\n')
			file.writelines(str(smurf) + '\n')
			file.write(str(back) + '\n')
			file.write(str(teardrop) + '\n')
			file.write(str(pod) + '\n')
			file.write(str(land) + '\n')
			file.writelines(str(anomaly))
			file.close()

			file=open('./file/trainset.txt','w')
			file.write(teststd)
			file.close()



