
import React from 'react';
import '../css/login.css';
import { Link, Redirect } from "react-router-dom";
import { userService as service } from '../service/user';
import { observer } from 'mobx-react';
import { message } from 'antd';
import { inject } from '../utils';

import 'antd/lib/message/style';

@inject({ service }) // {servie:service} => service=service
@observer
export default class Login extends React.Component {
    constructor(props) {
        super(props);
    }
    handleClick(event) {
        event.preventDefault();
        const [email, password] = event.target.form;
        this.props.service.login(email.value, password.value, this); // async
        //this.setState({'ret':ret})
    }

    render() {
        console.log('login render++++++++++++++++++++++');
        if (this.props.service.loggedin) return <Redirect to="/" />;
        // if (this.props.service.errMsg){
        //     message.info(this.props.service.errMsg, 5, ()=>this.props.service.errMsg='');
        // }
        let em = this.props.service.errMsg;

        return (<div className="login-page">
            <div className="form">
                <form className="login-form">
                    <input type="text" placeholder="邮箱" defaultValue="sunny@magedu.com" />
                    <input type="password" placeholder="密码" />
                    <button onClick={this.handleClick.bind(this)}>登录</button>
                    <p className="message">未注册? <Link to="/reg">请注册</Link></p>
                </form>
            </div>
        </div>);
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevProps.service.errMsg) {
            message.info(prevProps.service.errMsg, 5, () => prevProps.service.errMsg = '');
        }
    }
}



