import React from 'react';
import ReactDom from 'react-dom';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import Login from './component/login';
import Reg from './component/reg';
import Pub from './component/pub';
import L from './component/list';
import Detail from './component/detail';
import { Menu, Icon, Layout } from 'antd';
import { LocaleProvider } from 'antd';
import zh_CN from 'antd/lib/locale-provider/zh_CN';

const { Header, Footer, Content } = Layout;

import 'antd/lib/menu/style';
import 'antd/lib/icon/style';


function Home() {
  return (
    <div>
      <h2>Home</h2>
    </div>
  );
}

function About() {
  return (
    <div>
      <h2>About</h2>
    </div>
  );
}


class Root extends React.Component {
  render() {
    return (<Router>
      <Layout>
        <Header>
          <Menu mode="horizontal">
            <Menu.Item key="home"><Link to="/"><Icon type="home" />主页</Link></Menu.Item>
            <Menu.Item key="login"><Link to="/login"><Icon type="login" />登录</Link></Menu.Item>
            <Menu.Item key="reg"><Link to="/reg">注册</Link></Menu.Item>
            <Menu.Item key="pub"><Link to="/pub">发布</Link></Menu.Item>
            <Menu.Item key="list"><Link to="/list"><Icon type="bars" />文章列表</Link></Menu.Item>
            <Menu.Item key="about"><Link to="/about">关于我们</Link></Menu.Item>
          </Menu>
        </Header>
        <Content>
          <div style={{width:'80%', margin:'auto', padding:'5px', minHeight:200}}>
            <Route exact path="/" component={Home} />
            <Route path="/login" component={Login} />
            <Route path="/reg" component={Reg} />
            <Route path="/pub" component={Pub} />
            <Route path="/list" component={L} />            
            <Route path="/detail/:id" component={Detail} />            
            <Route path="/about" component={About} />
          </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>
          magedu.com ©2008-2018
        </Footer>



      </Layout>
    </Router>);
  }
}


ReactDom.render(<LocaleProvider locale={zh_CN}><Root /></LocaleProvider>, document.getElementById('root'));


