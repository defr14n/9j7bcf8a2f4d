import scrapy

class DmozSpider(scrapy.Spider):
	name = "dmoz"
	#html/div/table[@class='layouttab']/tbody/tr/td[contains(text(),'Website')]/following-sibling::td[1]
	url = raw_input("Masukkan Url: ")
	start_urls = [str(url)]

	def parse(self, response):
		filename = response.url.split("/")[-2]
		namafile = "cobalog.log"
		j = response.xpath('//body')
		keyword_ = raw_input("Masukkan Keyword: ")
		keyword = str(keyword_).lower()
		result = ''
		for k in j:
			#doc.xpath('/html/body//a[lower-case(text()) = "' + name.encode('utf8') + '"]/@href'
			a = j.xpath("//a/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			p = j.xpath("//p/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			#div = j.xpath("//div/text()").extract()
			div = j.xpath("//div/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			#div = j.xpath("//div[lower-case(text())]").extract()
			#div = j.xpath("//div/text()[contains(.,'Ronaldo')]").extract()
			h1 = j.xpath("//h1/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h2 = j.xpath("//h2/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h3 = j.xpath("//h3/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h4 = j.xpath("//h4/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h5 = j.xpath("//h5/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			h6 = j.xpath("//h6/text()[contains(translate(.,'ABCDEFGHIJKLMNOPURSTUWXYZ','abcdefghijklmnopurstuwxyz') , '" + keyword + "')]").extract()
			aj = ' '.join(a).strip() + " "
			pj = ' '.join(p).strip() + " "
			divj = ' '.join(div).strip() + " "
			h1j = ' '.join(h1).strip() + " "
			h2j = ' '.join(h2).strip() + " "
			h3j = ' '.join(h3).strip() + " "
			h4j = ' '.join(h4).strip() + " "
			h5j = ' '.join(h5).strip() + " "
			h6j = ' '.join(h6).strip() + " "
			result = "Content:  " + divj + " " + aj + " " + pj + " " + h1j + " " + h2j + " " + h3j + " " + h4j + " " + h5j + " " + h6j + " "
			spasi = 2
			hspasi = " "
			hspasi2 ="" 
			while spasi < 150:
				hspasi2 = hspasi2 + hspasi
				result.replace(hspasi2,"")
				spasi = spasi + 1
			#print result
		with open(namafile, 'a') as f:
			f.write("\n=========================================================================================================\n")
			f.write("url : " + response.url + "\n")
			f.write("-----------------------------------------------------------------------------------------------------------\n")
			f.write(result.encode('utf8').lower() + "\n=========================================================================================================\n")
			#print str(len(result)) +" "
			#print str(len(divj)) + " "
			#print str(len(pj)) + " "
			#print str(len(aj)) + " "
		
