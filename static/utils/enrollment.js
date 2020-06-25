function addClass({data = []}) {
    data.forEach(function (horario) {
        let color = horario["color"];
        let dia = horario['dia'];
        let titulo = horario['curso'];
        let sigla = horario['sigla'];
        let hinicio = horario['horainicio'].split(':')[0];
        let hfinal = horario['horafin'].split(':')[0];
        let limite = horario['limite'];
        let matriculados = horario['matriculados'];
        let lab = horario['laboratorio'];
        let id = '#' + lab + dia + hinicio;
        let id2 = '#' + lab + dia + ((hfinal - 1) < 10 ? '0' + (hfinal - 1) : (hfinal - 1));

        $(id).attr('rowspan', hfinal - hinicio);
        $(id).attr('data-toggle', "tooltip");
        $(id).attr('data-placement', "top");
        $(id).attr('title', titulo);
        $(id).attr('onclick', "elegirCurso({'id':'" + horario['id'] + "','dia':'" + dia + "','titulo':'" + titulo + "','hinicio':'" + horario['horainicio'] + "','hfinal':'" + horario['horafin'] + "'})");
        $(id).css({"background-color": color, "cursor": "pointer", "padding": "10px"});
        // $(id).append("<label style='font-weight: bold; font-size: 15px'>" + sigla + "<br><span> Karel</span><br><span id='" + dia + hinicio + "m'>" + matriculados + "</span> / <span> " + limite + "</span> </label>")
        $(id).append(sigla + "<br><span> Karel</span><br><span id='" + lab + dia + hinicio + "m'>" + matriculados + "</span> / <span> " + limite + "</span>");
        if (hfinal - hinicio === 3) {
            let idm = '#' + lab + dia + ((hfinal - 2) < 10 ? '0' + (hfinal - 2) : (hfinal - 2));
            $(idm).remove();
        }
        $(id2).remove();


    });
};

function updateClass({data = []}) {
    data.forEach(function (horario) {
        let hinicio = horario['horainicio'].split(':')[0];
        let dia = horario['dia'];
        let lab = horario['laboratorio'];
        let id = '#' + lab + dia + hinicio;
        let idm = '#' + lab + dia + hinicio + 'm';
        matr = horario['matriculados'];
        limite = horario['limite'];
        if (matr >= limite) {
            $(id).removeAttr("onclick");
            $(id).attr("onclick", "horarioCompleto()");

        }
        $(idm).text(matr);
    });

};

function horarioCompleto() {
    alert("EL horario ya esta completo");
}

function agregarClase() {

    let clase = [{
        "dia": $('#dia').val(),
        "title": $('#titulo').val(),
        "inicio": $('#hinicio').val().split(':')[0],
        "final": $('#hfinal').val().split(':')[0],
        "color": $('#color').val(),
    }]

    addClass({
        data: clase
    });
}

function elegirCurso(clase) {

    let ids = [];
    let row;
    let id = clase['id'];
    let curso = clase['titulo'];
    $('#horarioNuevo tr').each(function () {
        let pk = $(this).find("td").eq(1).html();
        if (pk !== undefined) {
            ids.push(pk);
        }
    });
    row = "<tr id='clase"
        + id + "'><td hidden>" + id + "</td><td>"
        + clase['titulo'] + "</td><td>"
        + clase['dia'] + "</td><td>"
        + clase['hinicio'] + "</td><td>"
        + clase['hfinal'] + "</td><td><a onclick='deleteClass(" + id + ")'><i class='fa fa-trash'></i></a></td></tr>"

    if (ids.length === 0) {
        $('#horarioNuevo tbody').append(row);
    } else {
        if (ids.includes(curso)) {
            alert("Clase ya agregada");
        } else {
            $('#horarioNuevo tbody').append(row);
        }
    }

}

function deleteClass(id) {
    e = '#clase' + id
    $(e).remove();
}

function generarTabla({days = [], startdate = 0, enddate = 0, laboratory = ""}) {

    //let dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado'];
    let head = "";
    let body = "";

    days.forEach(function (d) {
        head += "<th> " + d + " </th>"
    })

    for (let index = startdate; index < enddate; index++) {

        body += "<tr><th>" + index + ":00 - " + (index + 1) + ":00 </th>";


        days.forEach(function (d) {

            body += "<td style='text-align: center' id='" + laboratory + d.toLowerCase() + ((index < 10) ? '0' + index : index) + "'></td>"
        });
        body += "</tr>"

    }


    let tabla;
    return tabla = "<table class='table table-bordered jambo_table'>\n\
        <thead>\n\
            <tr>\n\
                <th></th>\n\
                " + head + "\n\
            </tr>\n\
        </thead>\n\
        <tbody>\n\
        " + body + "\n\
        </body>\n\
    </table>";
}