import scrapy
import time
#class untuk mengintputkan dari keyboard
class Inputan(object):
	def inKeyword(self,inputan):
		self._key = str(inputan)

	def getKeyword(self):
		return self._key

#class utama spider
class JjSpider(scrapy.Spider):
	name = "jj"
	Input = Inputan()
	#all variabel
	url = raw_input("Masukkan Url: ")
	aka = Input.inKeyword(raw_input("Masukkan Keyword: "))
		
	start_urls = [str(url)]
	
	def parse(self, response):
		
		filename = response.url.split("/")[-2]
		namafile = "log_scrapy_" + str(time.strftime("%d_%m_%Y")) + "_.log"
		j = response.xpath('//body')
		
		keyword = str(self.Input.getKeyword().lower())
		result = ''
		for k in j:
			#mengambil text dielemen  html yang mengandung keyword dan menjadikannya ke huruf kecil semua
			a = j.xpath("//a/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			p = j.xpath("//p/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			div = j.xpath("//div/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h1 = j.xpath("//h1/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h2 = j.xpath("//h2/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h3 = j.xpath("//h3/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h4 = j.xpath("//h4/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h5 = j.xpath("//h5/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h6 = j.xpath("//h6/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			span = j.xpath("//span/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			strong = j.xpath("//strong/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			#menggabung variabel diatas
			aj = ' '.join(a).strip() + " "
			pj = ' '.join(p).strip() + " "
			divj = ' '.join(div).strip() + " "
			h1j = ' '.join(h1).strip() + " "
			h2j = ' '.join(h2).strip() + " "
			h3j = ' '.join(h3).strip() + " "
			h4j = ' '.join(h4).strip() + " "
			h5j = ' '.join(h5).strip() + " "
			h6j = ' '.join(h6).strip() + " "
			spanj = ' '.join(span).strip() + " "
			strongj = ' '.join(strong).strip() + " "
			#menjadikannya jadi satu
			result = "Content:  " + divj + " " + aj + " " + pj + " " + h1j + " " + h2j + " " + h3j + " " + h4j + " " + h5j + " " + h6j + " " + spanj + " " + strongj
			
			
		with open(namafile, 'a') as f:
			f.write("=========================================================================================================\n")
			f.write("Url : " + response.url + "\n")
			f.write("Keyword: " + keyword + "\n")
			f.write("Matches Count: " + str(result.count(keyword)) + "\n")
			f.write("-----------------------------------------------------------------------------------------------------------\n")
			f.write(result.encode('utf8').lower())
			f.write("\n=========================================================================================================\n")
			#print str(len(result)) +" "
			#print str(len(divj)) + " "
			#print str(len(pj)) + " "
			#print str(len(aj)) + " "
		
