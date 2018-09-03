import React from 'react';
// import sinon from 'sinon';
// import { expect } from 'chai';
import Adapter from 'enzyme-adapter-react-16';
import Enzyme, { mount } from 'enzyme';

import Index from '../src/index.for-test'

// const sleep = timeout => new Promise((r, j) => setTimeout(r, timeout))
Enzyme.configure({ adapter: new Adapter() });

describe('mount Index', () => {
  it ('should success', () => {
    const app = mount(<Index />);
    const input = app.find('input').at(0).getDOMNode(0);

    input.value = 'hello world';

    const addBtn = app.find('button').at(0);
    addBtn.simulate('submit')

    const listUl = app.find('ul').at(0);
    console.log(listUl.find('li').at(0).props(), '-----xxx')
  })
})
