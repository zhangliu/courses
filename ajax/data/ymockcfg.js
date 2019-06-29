const fs = require('fs')

module.exports = [{
	pattern: /(.*?)$/,
	// respondWith: function(postData, qs, req, res){
	// 	const filename = qs.url.replace(/.*\/(.*?)$/, '$1')
	// 	const path = `${process.cwd()}/${filename}.js`
	// 	if (!fs.existsSync(path)) return `【错误】没有找到文件${path}!`
	// 	delete require.cache[path]
	// 	const data = require(path)
	// 	return data
	// }
	respondWith: './test.mockjson'
}]
