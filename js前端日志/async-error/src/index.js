// --------------------异步异常捕获-------------------------
// async function test1() {
//   try {
//     await err(new Error(), test2())
//   } catch (e) {
//     console.log(e)
//     // console.log(e.stack.replace(/\n/g, '&'))
//   }
// }

// async function test2() {
//   return err(new Error(), test3())
// }

// async function test3() {
//     JSON.parse('x')
// }

// async function err(error, promise) {
//   try {
//     return await promise
//   } catch (e) {
//     const indexStr = error.stack.split('\n')[1]
//     e.stack = `${e.stack}\n${indexStr}`
//     throw e
//   }
// }

// test1()


