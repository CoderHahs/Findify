import React from 'react';
import './NameInput.css';

const api = process.env.REACT_APP_ONO_API;

class NameInput extends React.Component {
    constructor(props) {
        super(props);
        this.state = { firstname: '', lastname: '', items: {} };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        var name = event.target.value.split(" ");
        var fn = name[0];
        var ln = name[1];
        this.setState({ firstname: fn, lastname: ln });
    }

    handleSubmit(event) {
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
        console.log(this.state.items)
        document.getElementById('thanks').innerHTML = 'A name was submitted: ' + this.state.firstname + ' ' + this.state.lastname;
        event.preventDefault();
    }

    render() {
        return (
            <div className="container">
                <div className="inner-container">
                    <form onSubmit={this.handleSubmit}>
                        <input type='text' id='name-input' value={this.state.value} onChange={this.handleChange}></input>
                        <input type="submit" value="Submit" on />
                        <h2 id='thanks'> </h2>
                    </form>
                </div>
            </div>
        );
    }
}


export default NameInput;