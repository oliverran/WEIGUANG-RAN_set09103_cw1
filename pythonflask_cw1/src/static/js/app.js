function requestJSON(url, callback) {
  $.ajax({
    url: url,
    complete: function(xhr) {
      callback.call(null, xhr.responseJSON);
    }
  });
}

