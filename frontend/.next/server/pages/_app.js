/*
 * ATTENTION: An "eval-source-map" devtool has been used.
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file with attached SourceMaps in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
(() => {
var exports = {};
exports.id = "pages/_app";
exports.ids = ["pages/_app"];
exports.modules = {

/***/ "./styles/Form.css":
/*!*************************!*\
  !*** ./styles/Form.css ***!
  \*************************/
/***/ (() => {



/***/ }),

/***/ "next/dist/compiled/next-server/pages.runtime.dev.js":
/*!**********************************************************************!*\
  !*** external "next/dist/compiled/next-server/pages.runtime.dev.js" ***!
  \**********************************************************************/
/***/ ((module) => {

"use strict";
module.exports = require("next/dist/compiled/next-server/pages.runtime.dev.js");

/***/ }),

/***/ "react":
/*!************************!*\
  !*** external "react" ***!
  \************************/
/***/ ((module) => {

"use strict";
module.exports = require("react");

/***/ }),

/***/ "react-dom":
/*!****************************!*\
  !*** external "react-dom" ***!
  \****************************/
/***/ ((module) => {

"use strict";
module.exports = require("react-dom");

/***/ }),

/***/ "react/jsx-dev-runtime":
/*!****************************************!*\
  !*** external "react/jsx-dev-runtime" ***!
  \****************************************/
/***/ ((module) => {

"use strict";
module.exports = require("react/jsx-dev-runtime");

/***/ }),

/***/ "react/jsx-runtime":
/*!************************************!*\
  !*** external "react/jsx-runtime" ***!
  \************************************/
/***/ ((module) => {

"use strict";
module.exports = require("react/jsx-runtime");

/***/ }),

/***/ "fs":
/*!*********************!*\
  !*** external "fs" ***!
  \*********************/
/***/ ((module) => {

"use strict";
module.exports = require("fs");

/***/ }),

/***/ "stream":
/*!*************************!*\
  !*** external "stream" ***!
  \*************************/
/***/ ((module) => {

"use strict";
module.exports = require("stream");

/***/ }),

/***/ "zlib":
/*!***********************!*\
  !*** external "zlib" ***!
  \***********************/
/***/ ((module) => {

"use strict";
module.exports = require("zlib");

/***/ }),

/***/ "axios":
/*!************************!*\
  !*** external "axios" ***!
  \************************/
/***/ ((module) => {

"use strict";
module.exports = import("axios");;

/***/ }),

/***/ "jwt-decode":
/*!*****************************!*\
  !*** external "jwt-decode" ***!
  \*****************************/
/***/ ((module) => {

"use strict";
module.exports = import("jwt-decode");;

/***/ }),

/***/ "./api.js":
/*!****************!*\
  !*** ./api.js ***!
  \****************/
/***/ ((__webpack_module__, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.a(__webpack_module__, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {\n__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (__WEBPACK_DEFAULT_EXPORT__)\n/* harmony export */ });\n/* harmony import */ var axios__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! axios */ \"axios\");\n/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ./constants */ \"./constants.js\");\nvar __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([axios__WEBPACK_IMPORTED_MODULE_0__]);\naxios__WEBPACK_IMPORTED_MODULE_0__ = (__webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__)[0];\n\n\n// Créer une instance de Axios\n// pour rediriger les requêtes vers notre serveur django REST framework.\nconst api = axios__WEBPACK_IMPORTED_MODULE_0__[\"default\"].create({\n    baseURL: \"http://127.0.0.1:8000\"\n});\n// Un interceptor pour ajouter l'authorization token à chaque requête\napi.interceptors.request.use(async (config)=>{\n    const accessToken = localStorage.getItem(_constants__WEBPACK_IMPORTED_MODULE_1__.ACCESS_TOKEN);\n    if (accessToken) {\n        config.headers.Authorization = `Bearer ${accessToken}`;\n    }\n    return config;\n}, (error)=>{\n    return Promise.reject(error);\n});\n//\n/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (api);\n\n__webpack_async_result__();\n} catch(e) { __webpack_async_result__(e); } });//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9hcGkuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7Ozs7O0FBQTBCO0FBQ2lCO0FBRTNDLDhCQUE4QjtBQUM5Qix3RUFBd0U7QUFDeEUsTUFBTUUsTUFBTUYsb0RBQVksQ0FBQztJQUNyQkksU0FBU0MsdUJBQStCO0FBQzVDO0FBR0EscUVBQXFFO0FBQ3JFSCxJQUFJTSxZQUFZLENBQUNDLE9BQU8sQ0FBQ0MsR0FBRyxDQUN4QixPQUFPQztJQUNILE1BQU1DLGNBQWNDLGFBQWFDLE9BQU8sQ0FBQ2Isb0RBQVlBO0lBQ3JELElBQUlXLGFBQWE7UUFDYkQsT0FBT0ksT0FBTyxDQUFDQyxhQUFhLEdBQUcsQ0FBQyxPQUFPLEVBQUVKLFlBQVksQ0FBQztJQUMxRDtJQUNBLE9BQU9EO0FBQ1gsR0FDQSxDQUFDTTtJQUNHLE9BQU9DLFFBQVFDLE1BQU0sQ0FBQ0Y7QUFDMUI7QUFHSixFQUFFO0FBQ0YsaUVBQWVmLEdBQUdBLEVBQUMiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL2FwaS5qcz84N2ZiIl0sInNvdXJjZXNDb250ZW50IjpbImltcG9ydCBheGlvcyBmcm9tIFwiYXhpb3NcIjtcbmltcG9ydCB7IEFDQ0VTU19UT0tFTiB9IGZyb20gXCIuL2NvbnN0YW50c1wiO1xuXG4vLyBDcsOpZXIgdW5lIGluc3RhbmNlIGRlIEF4aW9zXG4vLyBwb3VyIHJlZGlyaWdlciBsZXMgcmVxdcOqdGVzIHZlcnMgbm90cmUgc2VydmV1ciBkamFuZ28gUkVTVCBmcmFtZXdvcmsuXG5jb25zdCBhcGkgPSBheGlvcy5jcmVhdGUoe1xuICAgIGJhc2VVUkw6IHByb2Nlc3MuZW52Lk5FWFRfUFVCTElDX0FQSV9VUkwsXG59KVxuXG5cbi8vIFVuIGludGVyY2VwdG9yIHBvdXIgYWpvdXRlciBsJ2F1dGhvcml6YXRpb24gdG9rZW4gw6AgY2hhcXVlIHJlcXXDqnRlXG5hcGkuaW50ZXJjZXB0b3JzLnJlcXVlc3QudXNlKFxuICAgIGFzeW5jIChjb25maWcpID0+IHtcbiAgICAgICAgY29uc3QgYWNjZXNzVG9rZW4gPSBsb2NhbFN0b3JhZ2UuZ2V0SXRlbShBQ0NFU1NfVE9LRU4pO1xuICAgICAgICBpZiAoYWNjZXNzVG9rZW4pIHtcbiAgICAgICAgICAgIGNvbmZpZy5oZWFkZXJzLkF1dGhvcml6YXRpb24gPSBgQmVhcmVyICR7YWNjZXNzVG9rZW59YDtcbiAgICAgICAgfVxuICAgICAgICByZXR1cm4gY29uZmlnO1xuICAgIH0sXG4gICAgKGVycm9yKSA9PiB7XG4gICAgICAgIHJldHVybiBQcm9taXNlLnJlamVjdChlcnJvcik7XG4gICAgfVxuKTtcblxuLy9cbmV4cG9ydCBkZWZhdWx0IGFwaTsiXSwibmFtZXMiOlsiYXhpb3MiLCJBQ0NFU1NfVE9LRU4iLCJhcGkiLCJjcmVhdGUiLCJiYXNlVVJMIiwicHJvY2VzcyIsImVudiIsIk5FWFRfUFVCTElDX0FQSV9VUkwiLCJpbnRlcmNlcHRvcnMiLCJyZXF1ZXN0IiwidXNlIiwiY29uZmlnIiwiYWNjZXNzVG9rZW4iLCJsb2NhbFN0b3JhZ2UiLCJnZXRJdGVtIiwiaGVhZGVycyIsIkF1dGhvcml6YXRpb24iLCJlcnJvciIsIlByb21pc2UiLCJyZWplY3QiXSwic291cmNlUm9vdCI6IiJ9\n//# sourceURL=webpack-internal:///./api.js\n");

/***/ }),

/***/ "./components/ProtectedRoute.js":
/*!**************************************!*\
  !*** ./components/ProtectedRoute.js ***!
  \**************************************/
/***/ ((__webpack_module__, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.a(__webpack_module__, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {\n__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ ProtectedRoute)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"react/jsx-dev-runtime\");\n/* harmony import */ var _api__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/api */ \"./api.js\");\n/* harmony import */ var _constants__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @/constants */ \"./constants.js\");\n/* harmony import */ var jwt_decode__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! jwt-decode */ \"jwt-decode\");\n/* harmony import */ var next_router__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! next/router */ \"./node_modules/next/router.js\");\n/* harmony import */ var react__WEBPACK_IMPORTED_MODULE_5__ = __webpack_require__(/*! react */ \"react\");\nvar __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([_api__WEBPACK_IMPORTED_MODULE_1__, jwt_decode__WEBPACK_IMPORTED_MODULE_3__]);\n([_api__WEBPACK_IMPORTED_MODULE_1__, jwt_decode__WEBPACK_IMPORTED_MODULE_3__] = __webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__);\n/* __next_internal_client_entry_do_not_use__ default auto */ \n\n\n\n\n\nfunction ProtectedRoute({ children }) {\n    const [isAuthorized, setIsAuthorized] = (0,react__WEBPACK_IMPORTED_MODULE_5__.useState)(null);\n    const router = (0,next_router__WEBPACK_IMPORTED_MODULE_4__.useRouter)();\n    (0,react__WEBPACK_IMPORTED_MODULE_5__.useEffect)(()=>{\n        auth().catch(()=>{\n            localStorage.setItem(\"redirectAfterLogin\", router.asPath); // Stocke la route demandée\n            setIsAuthorized(false);\n        });\n    }, []);\n    const refreshToken = async ()=>{\n        const refreshToken = localStorage.getItem(_constants__WEBPACK_IMPORTED_MODULE_2__.REFRESH_TOKEN);\n        try {\n            const res = await _api__WEBPACK_IMPORTED_MODULE_1__[\"default\"].post(\"/login/refresh/\", {\n                refresh: refreshToken\n            });\n            if (res.status === 200) {\n                localStorage.setItem(_constants__WEBPACK_IMPORTED_MODULE_2__.ACCESS_TOKEN, res.data.access);\n                setIsAuthorized(true);\n            } else {\n                setIsAuthorized(false);\n            }\n        } catch (error) {\n            console.error(error);\n            setIsAuthorized(false);\n        }\n    };\n    const auth = async ()=>{\n        const token = localStorage.getItem(_constants__WEBPACK_IMPORTED_MODULE_2__.ACCESS_TOKEN);\n        if (!token) {\n            setIsAuthorized(false);\n            return;\n        }\n        const decoded = (0,jwt_decode__WEBPACK_IMPORTED_MODULE_3__.jwtDecode)(token);\n        const tokenExpiration = decoded.exp;\n        const now = Date.now() / 1000;\n        if (tokenExpiration < now) {\n            await refreshToken();\n        } else {\n            setIsAuthorized(true);\n        }\n    };\n    if (isAuthorized === null) {\n        return /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(\"div\", {\n            children: \"Loading...\"\n        }, void 0, false, {\n            fileName: \"/home/ensai/Documents/ENSAI2A/conception-logiciel/Projet-Conception-Logicielle-Bookit/frontend/components/ProtectedRoute.js\",\n            lineNumber: 55,\n            columnNumber: 12\n        }, this);\n    }\n    if (!isAuthorized) {\n        router.push(\"/login\");\n        return null;\n    }\n    return children;\n}\n\n__webpack_async_result__();\n} catch(e) { __webpack_async_result__(e); } });//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9jb21wb25lbnRzL1Byb3RlY3RlZFJvdXRlLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7Ozs7O0FBRXdCO0FBQ2tDO0FBQ25CO0FBQ0M7QUFDSTtBQUU3QixTQUFTTyxlQUFlLEVBQUVDLFFBQVEsRUFBRTtJQUNqRCxNQUFNLENBQUNDLGNBQWNDLGdCQUFnQixHQUFHSiwrQ0FBUUEsQ0FBQztJQUNqRCxNQUFNSyxTQUFTUCxzREFBU0E7SUFFeEJDLGdEQUFTQSxDQUFDO1FBQ1JPLE9BQU9DLEtBQUssQ0FBQztZQUNYQyxhQUFhQyxPQUFPLENBQUMsc0JBQXNCSixPQUFPSyxNQUFNLEdBQUcsMkJBQTJCO1lBQ3RGTixnQkFBZ0I7UUFDbEI7SUFDRixHQUFHLEVBQUU7SUFFTCxNQUFNTyxlQUFlO1FBQ25CLE1BQU1BLGVBQWVILGFBQWFJLE9BQU8sQ0FBQ2hCLHFEQUFhQTtRQUN2RCxJQUFJO1lBQ0YsTUFBTWlCLE1BQU0sTUFBTW5CLGlEQUFRLENBQUMsbUJBQW1CO2dCQUFFcUIsU0FBU0o7WUFBYTtZQUN0RSxJQUFJRSxJQUFJRyxNQUFNLEtBQUssS0FBSztnQkFDdEJSLGFBQWFDLE9BQU8sQ0FBQ2Qsb0RBQVlBLEVBQUVrQixJQUFJSSxJQUFJLENBQUNDLE1BQU07Z0JBQ2xEZCxnQkFBZ0I7WUFDbEIsT0FBTztnQkFDTEEsZ0JBQWdCO1lBQ2xCO1FBQ0YsRUFBRSxPQUFPZSxPQUFPO1lBQ2RDLFFBQVFELEtBQUssQ0FBQ0E7WUFDZGYsZ0JBQWdCO1FBQ2xCO0lBQ0Y7SUFFQSxNQUFNRSxPQUFPO1FBQ1gsTUFBTWUsUUFBUWIsYUFBYUksT0FBTyxDQUFDakIsb0RBQVlBO1FBQy9DLElBQUksQ0FBQzBCLE9BQU87WUFDVmpCLGdCQUFnQjtZQUNoQjtRQUNGO1FBRUEsTUFBTWtCLFVBQVV6QixxREFBU0EsQ0FBQ3dCO1FBQzFCLE1BQU1FLGtCQUFrQkQsUUFBUUUsR0FBRztRQUNuQyxNQUFNQyxNQUFNQyxLQUFLRCxHQUFHLEtBQUs7UUFFekIsSUFBSUYsa0JBQWtCRSxLQUFLO1lBQ3pCLE1BQU1kO1FBQ1IsT0FBTztZQUNMUCxnQkFBZ0I7UUFDbEI7SUFDRjtJQUVBLElBQUlELGlCQUFpQixNQUFNO1FBQ3pCLHFCQUFPLDhEQUFDd0I7c0JBQUk7Ozs7OztJQUNkO0lBRUEsSUFBSSxDQUFDeEIsY0FBYztRQUNqQkUsT0FBT3VCLElBQUksQ0FBQztRQUNaLE9BQU87SUFDVDtJQUVBLE9BQU8xQjtBQUNUIiwic291cmNlcyI6WyJ3ZWJwYWNrOi8vZnJvbnRlbmQvLi9jb21wb25lbnRzL1Byb3RlY3RlZFJvdXRlLmpzPzQzYzUiXSwic291cmNlc0NvbnRlbnQiOlsiXCJ1c2UgY2xpZW50XCI7XG5cbmltcG9ydCBhcGkgZnJvbSBcIkAvYXBpXCI7XG5pbXBvcnQgeyBBQ0NFU1NfVE9LRU4sIFJFRlJFU0hfVE9LRU4gfSBmcm9tIFwiQC9jb25zdGFudHNcIjtcbmltcG9ydCB7IGp3dERlY29kZSB9IGZyb20gXCJqd3QtZGVjb2RlXCI7XG5pbXBvcnQgeyB1c2VSb3V0ZXIgfSBmcm9tIFwibmV4dC9yb3V0ZXJcIjtcbmltcG9ydCB7IHVzZUVmZmVjdCwgdXNlU3RhdGUgfSBmcm9tIFwicmVhY3RcIjtcblxuZXhwb3J0IGRlZmF1bHQgZnVuY3Rpb24gUHJvdGVjdGVkUm91dGUoeyBjaGlsZHJlbiB9KSB7XG4gIGNvbnN0IFtpc0F1dGhvcml6ZWQsIHNldElzQXV0aG9yaXplZF0gPSB1c2VTdGF0ZShudWxsKTtcbiAgY29uc3Qgcm91dGVyID0gdXNlUm91dGVyKCk7XG5cbiAgdXNlRWZmZWN0KCgpID0+IHtcbiAgICBhdXRoKCkuY2F0Y2goKCkgPT4ge1xuICAgICAgbG9jYWxTdG9yYWdlLnNldEl0ZW0oXCJyZWRpcmVjdEFmdGVyTG9naW5cIiwgcm91dGVyLmFzUGF0aCk7IC8vIFN0b2NrZSBsYSByb3V0ZSBkZW1hbmTDqWVcbiAgICAgIHNldElzQXV0aG9yaXplZChmYWxzZSk7XG4gICAgfSk7XG4gIH0sIFtdKTtcblxuICBjb25zdCByZWZyZXNoVG9rZW4gPSBhc3luYyAoKSA9PiB7XG4gICAgY29uc3QgcmVmcmVzaFRva2VuID0gbG9jYWxTdG9yYWdlLmdldEl0ZW0oUkVGUkVTSF9UT0tFTik7XG4gICAgdHJ5IHtcbiAgICAgIGNvbnN0IHJlcyA9IGF3YWl0IGFwaS5wb3N0KFwiL2xvZ2luL3JlZnJlc2gvXCIsIHsgcmVmcmVzaDogcmVmcmVzaFRva2VuIH0pO1xuICAgICAgaWYgKHJlcy5zdGF0dXMgPT09IDIwMCkge1xuICAgICAgICBsb2NhbFN0b3JhZ2Uuc2V0SXRlbShBQ0NFU1NfVE9LRU4sIHJlcy5kYXRhLmFjY2Vzcyk7XG4gICAgICAgIHNldElzQXV0aG9yaXplZCh0cnVlKTtcbiAgICAgIH0gZWxzZSB7XG4gICAgICAgIHNldElzQXV0aG9yaXplZChmYWxzZSk7XG4gICAgICB9XG4gICAgfSBjYXRjaCAoZXJyb3IpIHtcbiAgICAgIGNvbnNvbGUuZXJyb3IoZXJyb3IpO1xuICAgICAgc2V0SXNBdXRob3JpemVkKGZhbHNlKTtcbiAgICB9XG4gIH07XG5cbiAgY29uc3QgYXV0aCA9IGFzeW5jICgpID0+IHtcbiAgICBjb25zdCB0b2tlbiA9IGxvY2FsU3RvcmFnZS5nZXRJdGVtKEFDQ0VTU19UT0tFTik7XG4gICAgaWYgKCF0b2tlbikge1xuICAgICAgc2V0SXNBdXRob3JpemVkKGZhbHNlKTtcbiAgICAgIHJldHVybjtcbiAgICB9XG5cbiAgICBjb25zdCBkZWNvZGVkID0gand0RGVjb2RlKHRva2VuKTtcbiAgICBjb25zdCB0b2tlbkV4cGlyYXRpb24gPSBkZWNvZGVkLmV4cDtcbiAgICBjb25zdCBub3cgPSBEYXRlLm5vdygpIC8gMTAwMDtcblxuICAgIGlmICh0b2tlbkV4cGlyYXRpb24gPCBub3cpIHtcbiAgICAgIGF3YWl0IHJlZnJlc2hUb2tlbigpO1xuICAgIH0gZWxzZSB7XG4gICAgICBzZXRJc0F1dGhvcml6ZWQodHJ1ZSk7XG4gICAgfVxuICB9O1xuXG4gIGlmIChpc0F1dGhvcml6ZWQgPT09IG51bGwpIHtcbiAgICByZXR1cm4gPGRpdj5Mb2FkaW5nLi4uPC9kaXY+O1xuICB9XG5cbiAgaWYgKCFpc0F1dGhvcml6ZWQpIHtcbiAgICByb3V0ZXIucHVzaChcIi9sb2dpblwiKTtcbiAgICByZXR1cm4gbnVsbDtcbiAgfVxuXG4gIHJldHVybiBjaGlsZHJlbjtcbn1cbiJdLCJuYW1lcyI6WyJhcGkiLCJBQ0NFU1NfVE9LRU4iLCJSRUZSRVNIX1RPS0VOIiwiand0RGVjb2RlIiwidXNlUm91dGVyIiwidXNlRWZmZWN0IiwidXNlU3RhdGUiLCJQcm90ZWN0ZWRSb3V0ZSIsImNoaWxkcmVuIiwiaXNBdXRob3JpemVkIiwic2V0SXNBdXRob3JpemVkIiwicm91dGVyIiwiYXV0aCIsImNhdGNoIiwibG9jYWxTdG9yYWdlIiwic2V0SXRlbSIsImFzUGF0aCIsInJlZnJlc2hUb2tlbiIsImdldEl0ZW0iLCJyZXMiLCJwb3N0IiwicmVmcmVzaCIsInN0YXR1cyIsImRhdGEiLCJhY2Nlc3MiLCJlcnJvciIsImNvbnNvbGUiLCJ0b2tlbiIsImRlY29kZWQiLCJ0b2tlbkV4cGlyYXRpb24iLCJleHAiLCJub3ciLCJEYXRlIiwiZGl2IiwicHVzaCJdLCJzb3VyY2VSb290IjoiIn0=\n//# sourceURL=webpack-internal:///./components/ProtectedRoute.js\n");

/***/ }),

/***/ "./constants.js":
/*!**********************!*\
  !*** ./constants.js ***!
  \**********************/
/***/ ((__unused_webpack___webpack_module__, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   ACCESS_TOKEN: () => (/* binding */ ACCESS_TOKEN),\n/* harmony export */   REFRESH_TOKEN: () => (/* binding */ REFRESH_TOKEN)\n/* harmony export */ });\nconst ACCESS_TOKEN = \"access\";\nconst REFRESH_TOKEN = \"refresh\";\n//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9jb25zdGFudHMuanMiLCJtYXBwaW5ncyI6Ijs7Ozs7QUFBTyxNQUFNQSxlQUFlLFNBQVU7QUFDL0IsTUFBTUMsZ0JBQWdCLFVBQVciLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL2NvbnN0YW50cy5qcz84OGYxIl0sInNvdXJjZXNDb250ZW50IjpbImV4cG9ydCBjb25zdCBBQ0NFU1NfVE9LRU4gPSBcImFjY2Vzc1wiIDtcbmV4cG9ydCBjb25zdCBSRUZSRVNIX1RPS0VOID0gXCJyZWZyZXNoXCIgOyJdLCJuYW1lcyI6WyJBQ0NFU1NfVE9LRU4iLCJSRUZSRVNIX1RPS0VOIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./constants.js\n");

/***/ }),

/***/ "./pages/_app.js":
/*!***********************!*\
  !*** ./pages/_app.js ***!
  \***********************/
/***/ ((__webpack_module__, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.a(__webpack_module__, async (__webpack_handle_async_dependencies__, __webpack_async_result__) => { try {\n__webpack_require__.r(__webpack_exports__);\n/* harmony export */ __webpack_require__.d(__webpack_exports__, {\n/* harmony export */   \"default\": () => (/* binding */ MyApp)\n/* harmony export */ });\n/* harmony import */ var react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! react/jsx-dev-runtime */ \"react/jsx-dev-runtime\");\n/* harmony import */ var _components_ProtectedRoute__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @/components/ProtectedRoute */ \"./components/ProtectedRoute.js\");\n/* harmony import */ var _styles_Form_css__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ../styles/Form.css */ \"./styles/Form.css\");\n/* harmony import */ var next_router__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! next/router */ \"./node_modules/next/router.js\");\nvar __webpack_async_dependencies__ = __webpack_handle_async_dependencies__([_components_ProtectedRoute__WEBPACK_IMPORTED_MODULE_1__]);\n_components_ProtectedRoute__WEBPACK_IMPORTED_MODULE_1__ = (__webpack_async_dependencies__.then ? (await __webpack_async_dependencies__)() : __webpack_async_dependencies__)[0];\n/* __next_internal_client_entry_do_not_use__ default auto */ \n\n\n\nfunction MyApp({ Component, pageProps }) {\n    const router = (0,next_router__WEBPACK_IMPORTED_MODULE_3__.useRouter)(); // Utilise le hook useRouter pour obtenir le router\n    const protectedRoutes = [\n        \"/home\"\n    ];\n    const isProtected = protectedRoutes.includes(router.pathname); // Utilise router.pathname\n    return isProtected ? /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(_components_ProtectedRoute__WEBPACK_IMPORTED_MODULE_1__[\"default\"], {\n        children: /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(Component, {\n            ...pageProps\n        }, void 0, false, {\n            fileName: \"/home/ensai/Documents/ENSAI2A/conception-logiciel/Projet-Conception-Logicielle-Bookit/frontend/pages/_app.js\",\n            lineNumber: 15,\n            columnNumber: 7\n        }, this)\n    }, void 0, false, {\n        fileName: \"/home/ensai/Documents/ENSAI2A/conception-logiciel/Projet-Conception-Logicielle-Bookit/frontend/pages/_app.js\",\n        lineNumber: 14,\n        columnNumber: 5\n    }, this) : /*#__PURE__*/ (0,react_jsx_dev_runtime__WEBPACK_IMPORTED_MODULE_0__.jsxDEV)(Component, {\n        ...pageProps\n    }, void 0, false, {\n        fileName: \"/home/ensai/Documents/ENSAI2A/conception-logiciel/Projet-Conception-Logicielle-Bookit/frontend/pages/_app.js\",\n        lineNumber: 18,\n        columnNumber: 5\n    }, this);\n}\n\n__webpack_async_result__();\n} catch(e) { __webpack_async_result__(e); } });//# sourceURL=[module]\n//# sourceMappingURL=data:application/json;charset=utf-8;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiLi9wYWdlcy9fYXBwLmpzIiwibWFwcGluZ3MiOiI7Ozs7Ozs7Ozs7OztBQUV5RDtBQUM3QjtBQUVZO0FBRXpCLFNBQVNFLE1BQU0sRUFBRUMsU0FBUyxFQUFFQyxTQUFTLEVBQUU7SUFDcEQsTUFBTUMsU0FBU0osc0RBQVNBLElBQUssbURBQW1EO0lBQ2hGLE1BQU1LLGtCQUFrQjtRQUFDO0tBQVE7SUFDakMsTUFBTUMsY0FBY0QsZ0JBQWdCRSxRQUFRLENBQUNILE9BQU9JLFFBQVEsR0FBRywwQkFBMEI7SUFFekYsT0FBT0YsNEJBQ0wsOERBQUNQLGtFQUFjQTtrQkFDYiw0RUFBQ0c7WUFBVyxHQUFHQyxTQUFTOzs7Ozs7Ozs7OzZCQUcxQiw4REFBQ0Q7UUFBVyxHQUFHQyxTQUFTOzs7Ozs7QUFFNUIiLCJzb3VyY2VzIjpbIndlYnBhY2s6Ly9mcm9udGVuZC8uL3BhZ2VzL19hcHAuanM/ZTBhZCJdLCJzb3VyY2VzQ29udGVudCI6WyJcInVzZSBjbGllbnRcIjtcblxuaW1wb3J0IFByb3RlY3RlZFJvdXRlIGZyb20gXCJAL2NvbXBvbmVudHMvUHJvdGVjdGVkUm91dGVcIjtcbmltcG9ydCAnLi4vc3R5bGVzL0Zvcm0uY3NzJztcblxuaW1wb3J0IHsgdXNlUm91dGVyIH0gZnJvbSAnbmV4dC9yb3V0ZXInO1xuXG5leHBvcnQgZGVmYXVsdCBmdW5jdGlvbiBNeUFwcCh7IENvbXBvbmVudCwgcGFnZVByb3BzIH0pIHtcbiAgY29uc3Qgcm91dGVyID0gdXNlUm91dGVyKCk7ICAvLyBVdGlsaXNlIGxlIGhvb2sgdXNlUm91dGVyIHBvdXIgb2J0ZW5pciBsZSByb3V0ZXJcbiAgY29uc3QgcHJvdGVjdGVkUm91dGVzID0gW1wiL2hvbWVcIl07XG4gIGNvbnN0IGlzUHJvdGVjdGVkID0gcHJvdGVjdGVkUm91dGVzLmluY2x1ZGVzKHJvdXRlci5wYXRobmFtZSk7IC8vIFV0aWxpc2Ugcm91dGVyLnBhdGhuYW1lXG5cbiAgcmV0dXJuIGlzUHJvdGVjdGVkID8gKFxuICAgIDxQcm90ZWN0ZWRSb3V0ZT5cbiAgICAgIDxDb21wb25lbnQgey4uLnBhZ2VQcm9wc30gLz5cbiAgICA8L1Byb3RlY3RlZFJvdXRlPlxuICApIDogKFxuICAgIDxDb21wb25lbnQgey4uLnBhZ2VQcm9wc30gLz5cbiAgKTtcbn1cbiJdLCJuYW1lcyI6WyJQcm90ZWN0ZWRSb3V0ZSIsInVzZVJvdXRlciIsIk15QXBwIiwiQ29tcG9uZW50IiwicGFnZVByb3BzIiwicm91dGVyIiwicHJvdGVjdGVkUm91dGVzIiwiaXNQcm90ZWN0ZWQiLCJpbmNsdWRlcyIsInBhdGhuYW1lIl0sInNvdXJjZVJvb3QiOiIifQ==\n//# sourceURL=webpack-internal:///./pages/_app.js\n");

/***/ })

};
;

// load runtime
var __webpack_require__ = require("../webpack-runtime.js");
__webpack_require__.C(exports);
var __webpack_exec__ = (moduleId) => (__webpack_require__(__webpack_require__.s = moduleId))
var __webpack_exports__ = __webpack_require__.X(0, ["vendor-chunks/next","vendor-chunks/@swc"], () => (__webpack_exec__("./pages/_app.js")));
module.exports = __webpack_exports__;

})();