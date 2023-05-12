$(document).ready(function () {
    $("#foto_perfil").click(function () {
        if (!window.location.pathname.includes("detalhe_questao"))
            window.location.href = 'editar_foto_perfil';
    });
});
