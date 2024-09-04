Here is an example of Python Flask API code that implements the given user story:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for loan applications
loan_applications = []

# Route to create a new loan application
@app.route('/loan_applications', methods=['POST'])
def create_loan_application():
    data = request.get_json()
    applicant_id = data.get('applicant_id')
    
    # Check if the applicant already has an active loan application
    for application in loan_applications:
        if application['applicant_id'] == applicant_id and application['status'] == 'active':
            return jsonify({'message': 'Applicant already has an active loan application'}), 400
    
    # Create a new loan application
    loan_application = {
        'applicant_id': applicant_id,
        'status': 'active',
        'details': data.get('details')
    }
    loan_applications.append(loan_application)
    
    return jsonify({'message': 'Loan application created successfully'}), 201

# Route to get all loan applications associated with a single applicant
@app.route('/loan_applications/<applicant_id>', methods=['GET'])
def get_loan_applications(applicant_id):
    applications = []
    
    # Find all loan applications associated with the applicant
    for application in loan_applications:
        if application['applicant_id'] == applicant_id:
            applications.append(application)
    
    return jsonify(applications), 200

# Route to update the status of a loan application
@app.route('/loan_applications/<applicant_id>/<application_id>', methods=['PUT'])
def update_loan_application(applicant_id, application_id):
    data = request.get_json()
    new_status = data.get('status')
    
    # Find the loan application to update
    for application in loan_applications:
        if application['applicant_id'] == applicant_id and application['id'] == application_id:
            application['status'] = new_status
            return jsonify({'message': 'Loan application updated successfully'}), 200
    
    return jsonify({'message': 'Loan application not found'}), 404

if __name__ == '__main__':
    app.run()
```

This code defines three routes:
- `/loan_applications` (POST): Creates a new loan application. It checks if the applicant already has an active loan application before creating a new one.
- `/loan_applications/<applicant_id>` (GET): Retrieves all loan applications associated with a single applicant.
- `/loan_applications/<applicant_id>/<application_id>` (PUT): Updates the status of a loan application.

You can run this Flask API code by executing the script. The API will be accessible at `http://localhost:5000`. Please note that this code only provides a basic implementation and may need to be extended or modified to meet specific requirements.