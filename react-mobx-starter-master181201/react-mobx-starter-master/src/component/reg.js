
import React from 'react';
import '../css/login.css';
import { Link, Redirect } from "react-router-dom";
import { userService as service } from '../service/user';
import { observer } from 'mobx-react';
import { inject } from '../utils';

import 'antd/lib/message/style';

@inject({ service })
@observer
export default class Reg extends React.Component {
  validatePwd(pwd1, pwd2) {
    return pwd1.value === pwd2.value;
  }

  handleClick(event) {
    event.preventDefault();
    const [email, name, password, confirm] = event.target.form;
    console.log(email);
    console.log(name);
    console.log(password);
    console.log(confirm);
    if (this.validatePwd(password, confirm))
      this.props.service.reg(email.value, name.value, password.value);
    else {
      console.log('error~~~~~~~~~~~~~~~~')
    }
  }
  render() {
    console.log('reg page', this.props.service.loggedin)
    if (this.props.service.loggedin) return <Redirect to="/" />;
    let em = this.props.service.errMsg;

    return (<div className="login-page">
      <div className="form">
        <form className="register-form">
          <input type="text" placeholder="邮箱" />
          <input type="text" placeholder="用户名" />
          <input type="password" placeholder="密码" />
          <input type="password" placeholder="确认密码" />
          <button onClick={this.handleClick.bind(this)}>注册</button>
          <p className="message">已经注册? <Link to="/login">请登录</Link></p>
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
