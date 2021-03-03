import React from 'react';
import { Link, Redirect } from "react-router-dom";
import { postService as service } from '../service/post';
import { observer } from 'mobx-react';
import { message } from 'antd';
import { inject } from '../utils';

import { Form, Input, Button } from 'antd';

const FormItem = Form.Item;
const { TextArea } = Input;

import 'antd/lib/message/style';
import 'antd/lib/form/style';
import 'antd/lib/input/style';
import 'antd/lib/button/style';

@inject({ service }) // {servie:service} => service=service
@observer
export default class Pub extends React.Component {
    handleSubmit(event) {
        event.preventDefault();
        const [title, content] = event.target;
        this.props.service.pub(title.value, content.value);
    }

    render() {
        const formItemLayout = {
            labelCol: { span: 4 },
            wrapperCol: { span: 14 },
        };

        let msg = this.props.service.msg;
        return (
            <Form layout="horizontal" onSubmit={this.handleSubmit.bind(this)}>
                <FormItem label="标题"  {...formItemLayout}>
                    <Input placeholder="标题" />
                </FormItem >
                <FormItem label="内容" labelCol={{ span: 4 }} wrapperCol={{ span: 14 }}>
                    <TextArea rows={10} placeholder="内容" />
                </FormItem>
                <FormItem wrapperCol={{ span: 14, offset:8 }} >
                    <Button type="primary" htmlType="submit">
                        发布
                    </Button>
                </FormItem>
            </Form>
        );
    }

    componentDidUpdate(prevProps, prevState) {
        if (prevProps.service.msg) {
            message.info(prevProps.service.msg, 5, () => prevProps.service.msg = '');
        }
    }
}


