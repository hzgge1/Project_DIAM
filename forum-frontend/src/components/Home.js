import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QuestaoLista from "./QuestaoLista";
import axios from "axios"; //(12)
import { API_URL_QUESTOES } from "../constants";
//(13)
class Home extends Component { //(14)
    state = { //(15)
        questoes: [],
    };
    componentDidMount() { //(16)
        this.resetState();
    }
    getQuestoes = () => {
        axios.get(API_URL_QUESTOES).then(res => this.setState({ questoes:
            res.data })); //(17)
    };
    resetState = () => { //(16)
        this.getQuestoes();
    };
    render() {
        return (
            <Container style={{ marginTop: "20px" }}>
                <Row>
                    <Col>
                        <QuestaoLista
                            questoes={this.state.questoes}
                            resetState={this.resetState}
                        />
                    </Col>
                </Row>
            </Container>
        );
    }
}
export default Home;