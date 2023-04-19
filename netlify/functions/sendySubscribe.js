const API_ENDPOINT = process.env.SENDY_API
import fetch from 'node-fetch'

exports.handler = async (event, context) => {

    // Exclude any non-POST requests
    if (event.httpMethod != "POST") {
        return {
            statusCode: 405,
            body: "Request method used is not permitted"
        }
    }

    // Parse the form
    try {
        // NB: Using `var` since `const` is block-scoped
        var body = JSON.parse(event.body)
    }
    catch (e) {
        return {
            statusCode: 200,
            body: JSON.stringify({
                status: 400,
                type: "Error",
                body: `Invalid JSON - ${e.message}`
            })
        }
    }

    // Filter form data
    try {
        if ( !body.email || body.validation !== "" || !body.list ) throw 'Required fields not provided'
    }
    catch (e) {
        return {
            statusCode: 200,
            body: JSON.stringify({
                status: 409,
                type: "Error",
                body: `${e}`
            })
        }
    }

    // Subscribe email address
    const params = {
        api_key: process.env.SENDY_API_KEY,
        list: body.list,
        email: body.email,
        boolean: true
    }

    let formBody = [];
    for (const property in params) {
        const encodedKey = encodeURIComponent(property);
        const encodedValue = encodeURIComponent(params[property]);
        formBody.push(encodedKey + "=" + encodedValue);
    }
    formBody = formBody.join("&");

    try {
        const response = await fetch(API_ENDPOINT, {
            method: 'POST',
            body: formBody,
            headers: {
                "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
            }
        })
        const data = await response.text()

        if(data == "1" )
            return {
                statusCode: 200,
                body: JSON.stringify({
                    status: 200,
                    type: "Success",
                    body: `${body.email} has been subscribed.`
                })
            }
        else if(data=="Some fields are missing.")
            return {
                statusCode: 200,
                body: JSON.stringify({
                    status: 400,
                    type: "Error",
                    body: `Please fill in your name and email.`
                })
            }
        else if(data=="Invalid email address.")
            return {
                statusCode: 200,
                body: JSON.stringify({
                    status: 400,
                    type: "Error",
                    body: `Email address is invalid.`
                })
            }
        else if(data=="Already subscribed.")
            return {
                statusCode: 200,
                body: JSON.stringify({
                    status: 400,
                    type: "Error",
                    body: `Email address is already subscribed.`
                })
            }        
    } catch(error) {
        console.log('Fetch error: ', error)
        return {
            statusCode: 200,
            body: JSON.stringify({
                status: 500,
                type: "Error",
                body: `Unable to subscribe, please try again later.`
            })
        }
    }
}

