import React, { Component } from "react";
import { Table } from "reactstrap";

class QuestaoLista extends Component {
    render() {
        const questoes = this.props.questoes; {}
        return (
            <Table light> {}
                <thead> {}
                <tr>
                    <th>Questões</th>
                    <th>Descrição</th>
                    <th></th>
                </tr>
                </thead>
                <tbody> {}
                {!questoes || questoes.length <= 0 ? (
                    <tr>
                        <td colSpan="6" align="center">
                            <b>Não há questões</b>

                        </td>
                    </tr>
                ) : (
                    questoes.map(questao => (
                        <tr key={questao.pk}>
                            <td>{questao.questao_titulo}</td>
                            <td>{questao.questao_descricao}</td>
                        </tr>
                    ))
                )}
                </tbody>
            </Table>
        );
    }
}
export default QuestaoLista;