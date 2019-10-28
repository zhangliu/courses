// 类型检测
let height: number
height = 100 // success
height = '100' // fail
height = undefined // success
height = null // success

/**
 * 
 *   ------------------------------------------------
 *  |              number | string | boolen | ...    |
 *  |                                                |
 *  |                                                |
 *  |      ------                -----------         |
 *  |     | null |              | undefined |        |
 *  |      ------                -----------         |
 *   ------------------------------------------------
 * 
*/