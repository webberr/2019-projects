exports.myHandler = function(event, context, callback) {
	var foo = event.foo;
	var bar = event.bar;
	var result = MyLambdaFunction (foo, bar);
 
	callback(null, result);
}
 
function MyLambdaFunction (foo, bar) {
	// MyLambdaFunction logic here
}