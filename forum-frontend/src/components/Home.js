import React, { Component } from "react";
import { Col, Container, Row } from "reactstrap";
import QuestaoLista from "./QuestaoLista";
import axios from "axios";
import { API_URL_QUESTOES } from "../constants";
import myImage from '../static/images/model.png';

class Home extends Component {
    state = {
        questoes: []
    };
    componentDidMount() {
        this.resetState();
    }
    getQuestoes = () => {
        axios.get(API_URL_QUESTOES).then(res => this.setState({ questoes:
            res.data }));

    };

    resetState = () => {
        this.getQuestoes();
    };
    render() {
        return (
            <div className="index_content">
                <div className="left">
                    <div className="texto_introducao">
                        <h2>"Connecting coders, clarifying code."</h2>
                        <p>Clarify is a forum for all things related to coding. With a community of
                            passionate coders, you can find resources on a wide range of programming
                            languages and frameworks. Collaborate, ask questions, and share your knowledge
                            with other developers. Join Clarify today and explore the exciting world of coding!</p>
                    </div>

                    <Container style={{
                        marginTop: "100px",
                        overflow: "auto",
                        height: "400px"
                    }}>
                        <Row>
                            <Col>
                                <QuestaoLista
                                    questoes={this.state.questoes}
                                    resetState={this.resetState}
                                />
                            </Col>
                        </Row>
                    </Container>
                </div>
                <div className="right">
                    <img src={myImage} alt=""/>
                </div>
            </div>

        );
    }
}
export default Home;