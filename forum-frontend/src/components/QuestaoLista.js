import React, { Component } from "react";
import { Table } from "reactstrap";
class QuestaoLista extends Component {
    render() {
        const questoes = this.props.questoes; {/* (20) */}
        const opcoes = this.props.opcoes;
        return (
            <Table light> {/* (21) */}
                <thead> {/* (22) */}
                <tr>
                    <th>Texto</th>
                    <th>Data de criação</th>
                    <th></th>
                </tr>
                </thead>
                <tbody> {/* (23) */}
                {!questoes || questoes.length <= 0 ? (
                    <tr>
                        <td colSpan="6" align="center">
                            <b>Não há questões</b>
                        </td>
                    </tr>
                ) : (
                    questoes.map(questao => ( // (24)
                        <tr key={questao.pk}>
                            <td>{questao.questao_titulo}</td>
                            <td>{questao.questao_data}</td>
                        </tr>
                    ))
                )}
                </tbody>
            </Table>
        );
    }
}
export default QuestaoLista;