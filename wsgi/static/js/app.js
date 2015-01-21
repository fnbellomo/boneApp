(function(){
    var app = angular.module('analisis', ['ui.bootstrap']);

    /* con esto, cambio la sintaxis en html de angujar.js de `{{ }}` a `{[ ]}`
       para no tener conflico con jinja2 */
    app.config(['$interpolateProvider', function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[');
	$interpolateProvider.endSymbol(']}');
    }]);

    app.controller('CollapseCtrl', function ($scope) {
	$scope.isCollapsed = false;
	$scope.isCollapsed2 = false;
	$scope.isCollapsed3 = false;
	$scope.isCollapsed4 = false;
	$scope.isCollapsed5 = false;
    });

    app.controller('OffNavCollapseCtrl', function ($scope) {
	$scope.isNavCollapsed = true;
	$scope.isNavCollapsed2 = true;
	$scope.isNavCollapsed3 = true;
	$scope.isNavCollapsed4 = true;
	$scope.isNavCollapsed5 = true;
    });

})();