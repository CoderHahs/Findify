import React from 'react';
import './NameInput.css';

const api = process.env.REACT_APP_ONO_API;

class NameInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = { firstname: '', lastname: '', age: 0, items: {} };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        var name = event.target.value.split(" ");
        var fn = name[0];
        var ln = name[1];
        this.setState({ firstname: fn, lastname: ln, age: event.target.age });
    }

    handleSubmit(event) {
        console.log(this.state);
        const proxyurl = "https://cors-anywhere.herokuapp.com/";
        const url = 'https://ono.4b.rs/v1/nat?key=' + api + '&fn=' + this.state.firstname + '&sn=' + this.state.lastname + '&sanitize=1'; // site that doesn’t send Access-Control-*
        fetch(proxyurl + url)
            .then(response => response.json())
            .then(
                (response) => {
                    this.setState({
                        items: response
                    });
                },
            )
        console.log(typeof this.state.items)
        if (JSON.stringify(this.state.items) === JSON.stringify({})) {
            alert('empty')
        }
        else {
            document.getElementById('thanks').innerHTML = 'Origin:' + JSON.stringify(this.state.items.countries[0]['jurisdiction']);
        }
        event.preventDefault();
    }

    render() {
        return (
            <div className="container">
                <div className="inner-container">
                    <form onSubmit={this.handleSubmit}>
                        <input type='text' id='name-input' value={this.state.value} onChange={this.handleChange}></input>
                        <input type='number' id='age-input' value={this.state.age} onChange={this.handleChange}></input>
                        <input type="submit" value="Submit" on />
                        <h2 id='thanks'> </h2>
                    </form>
                </div>
            </div>
        );
    }
}


export default NameInput;