
import React from 'react';
import { Link, Redirect } from "react-router-dom";
import { postService as service } from '../service/post';
import { observer } from 'mobx-react';
import { message, Card } from 'antd';
import { inject } from '../utils';

import 'antd/lib/message/style';
import 'antd/lib/card/style';


@inject({ service }) // {servie:service} => service=service
@observer
export default class Detail extends React.Component {
    constructor(props) {
        super(props);
        console.log(props);
        const { id = -1 } = props.match.params;
        props.service.getPost(id);
    }

    render() {
        const { post_id, title, author, author_id, postdate, content } = this.props.service.post;
        console.log(postdate);
        if (title) {
            return (<Card title={title} style={{ width: '100%' }}              >
                <p>{author} {new Date(postdate).toLocaleString()}</p>
                <p>{content}</p>
            </Card>);
        } else
            return <div>无内容</div>

    }
}





