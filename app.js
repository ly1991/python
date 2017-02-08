var http = require("http");
var cheerio = require("cheerio");
var fs = require("fs");

var queryHref = "http://www.haha.mx/topic/1/new/";
var querySearch = 1;
var urls = [];

var sumCount = 0;
var reptCount = 0;
var downCount = 0;

function downImg(imgurl) {
	var narr = imgurl.replace("http://image.haha.mx/", "").split("/")
	// 做一步优化，如果存在文件，则不下载
	var filename = "./upload/topic1/" + narr[0]  + narr[1] + narr[2] + "_" + narr[4];
	fs.exists(filename, function(b){
		if (!b) {
			// 文件不存则进行 下载
			http.get(imgurl.replace("/small/", "/big/"), function(res) {
				var imgData = "";
				//一定要设置response的编码为binary否则会下载下来的图片打不开
				res.setEncoding("binary"); 
		
				res.on("data", function(chunk) {
					imgData += chunk;
				});
				
				res.on("end", function() {
					var savePath = "./upload/topic2/" + narr[0]  + narr[1] + narr[2] + "_" + narr[4];
					fs.writeFile(savePath, imgData, "binary", function(err) {
						if(err) {
							console.log(err);
						}  else {
							console.log(narr[0]  + narr[1] + narr[2] + "_" + narr[4]);
							if (urls.length > 0) {
								downImg(urls.shift());
								downCount++;
								console.log("剩余图片数量: "+urls.length);
							}
						}
					});
				});
			});
		} else {
			// 统计重复的图片
			console.log("该图片已经存在重复.");
			reptCount++;
			if (urls.length > 0) {
				downImg(urls.shift());
			}
		}
	});
	
	if (urls.length <= 0) {
		console.log("下载完毕");
		console.log("重复图片：" + reptCount);
		console.log("实际下载：" + downCount);
	}
}

//获取分页内容
function getHtml(href,search){
	console.log("正在获取第" + search + "页图片");
	var req = http.get(href+search, function(res){
			var data = "";
			res.setEncoding("utf8");

			res.on("data",function(chunk){
				data += chunk;
			});

			res.on("end",function(){
				$ = cheerio.load(data);
				var html = $(".joke-list-item .joke-main-content a img");
				
				for(var i=0;i<html.length;i++){
					var src = html[i].attribs.src;
					if(src.indexOf("http://image.haha.mx") > -1){
						urls.push(html[i].attribs.src);
					}
				}

				if(search < pagemax){
					getHtml(href,++search);
				}else{
					console.log("图片链接获取完毕");
					console.log(urls);
					sumCount = urls.length;
					console.log("链接总数量： "+ sumCount);
					console.log("开始下载......");
					downImg(urls.shift());
				}
			});
	});
}

var pagemax = 30;		// 获取到多少页的内容
var startindex = 1;		// 从多少页开始获取

function start(){
	console.log("开始获取图片链接......");
	getHtml(queryHref,startindex);
}

start();