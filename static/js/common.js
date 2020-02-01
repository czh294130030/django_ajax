function common() {
}

common.get_id = function () {
    var url_array = window.location.href.split('/');
    var id = url_array[url_array.length - 1]
    return id;
}
common.padDate = function (value) {
    return value < 10 ? '0' + value : value;
}