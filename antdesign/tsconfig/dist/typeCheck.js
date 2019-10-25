// 类型检测
var height;
height = 100; // success
height = '100'; // fail
height = undefined; // success
height = null; // success
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
