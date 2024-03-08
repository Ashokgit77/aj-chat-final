$(document).ready(function() {
    $("#message-form").submit(function(e) {
      e.preventDefault();
      const message = $("#message").val();
      $("#messages").append(`<p>You: ${message}</p>`);
      $.post("/chat", { question: message }, function(data) {
        $("#messages").append(`<p>Chatbot: ${data.answer}</p>`);
        $("#message").val("");
      });
    });
  });