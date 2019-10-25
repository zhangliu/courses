var weight;
weight = undefined;
// ? 相当于 string | undefined
function getPeople(name) {
    return name || '';
}
getPeople('zhangsan');
getPeople(undefined);
// any
var school;
school = null;
school = undefined;
school = 'hello';
school = 3;
