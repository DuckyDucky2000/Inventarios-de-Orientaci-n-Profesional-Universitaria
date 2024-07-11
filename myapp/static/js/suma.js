$('#num1, #num2, #num3').on('input',function(e){
    $('#total_sum').val(parseInt($('#num1').val()) + parseInt($('#num2').val()) + parseInt($('#num3').val()));
});