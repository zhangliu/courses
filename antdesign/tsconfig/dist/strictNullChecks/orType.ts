let weight: number | undefined
weight = undefined

// ? 相当于 string | undefined
function getPeople(name?: string) {
  return name || ''
}

getPeople('zhangsan')
getPeople(undefined)

// any
let school: any
school = null // success
school = undefined // success
school = 'hello' // success
school = 3 // success