function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

let title;
let tagline;
let description;
let businessCategory;

document.getElementById('categoryForm').addEventListener('submit', function (e) {
    e.preventDefault();
    title = document.getElementById('title').value;
    tagline = document.getElementById('tagline').value;
    description = document.getElementById('description').value;
    businessCategory = document.getElementById('category').value;
    const category = document.getElementById('category').value;
    
    if (category) {
        showBusinessForm(category);
    }
});


function showBusinessForm(category) {
    document.getElementById('categoryForm').style.display = 'none';
    document.getElementById('businessForm').style.display = 'block';
    document.getElementById('formTitle').textContent = category + ' Business Registration';

    const specificFields = document.getElementById('categorySpecificFields');
    specificFields.innerHTML = '';

    switch (category) {
        case 'Restaurant':
            specificFields.innerHTML = `
        <div class="mb-3">
            <label for="minPrice" class="form-label">Minimum Price</label>
            <input type="number" class="form-control" id="minPrice" required>
        </div>
        <div class="mb-3">
            <label for="maxPrice" class="form-label">Maximum Price</label>
            <input type="number" class="form-control" id="maxPrice" required>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="delivery">
            <label class="form-check-label" for="delivery">Delivery Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="takeOut">
            <label class="form-check-label" for="takeOut">Take-out Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="airConditioning">
            <label class="form-check-label" for="airConditioning">Air Conditioning</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="wifi">
            <label class="form-check-label" for="wifi">Wi-Fi Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="pureVeg">
            <label class="form-check-label" for="pureVeg">Pure Vegetarian</label>
        </div>
    `;
            break;
        case 'Hotel':
            specificFields.innerHTML = `
        <div class="mb-3">
            <label for="minPrice" class="form-label">Minimum Price per Night</label>
            <input type="number" class="form-control" id="minPrice" required>
        </div>
        <div class="mb-3">
            <label for="maxPrice" class="form-label">Maximum Price per Night</label>
            <input type="number" class="form-control" id="maxPrice" required>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="roomService">
            <label class="form-check-label" for="roomService">Room Service Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="gym">
            <label class="form-check-label" for="gym">Gym Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="pool">
            <label class="form-check-label" for="pool">Swimming Pool</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="spa">
            <label class="form-check-label" for="spa">Spa Available</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="petFriendly">
            <label class="form-check-label" for="petFriendly">Pet Friendly</label>
        </div>
    `;
            break;
        case 'Automotive':
            specificFields.innerHTML = `
        <div class="mb-3">
            <label for="minPrice" class="form-label">Minimum Service Price</label>
            <input type="number" class="form-control" id="minPrice" required>
        </div>
        <div class="mb-3">
            <label for="maxPrice" class="form-label">Maximum Service Price</label>
            <input type="number" class="form-control" id="maxPrice" required>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="repairServices">
            <label class="form-check-label" for="repairServices">Repair Services</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="partsSales">
            <label class="form-check-label" for="partsSales">Parts Sales</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="towingService">
            <label class="form-check-label" for="towingService">Towing Service</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="carWash">
            <label class="form-check-label" for="carWash">Car Wash</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="appointmentRequired">
            <label class="form-check-label" for="appointmentRequired">Appointment Required</label>
        </div>
    `;
            break;
        case 'BeautySpa':
            specificFields.innerHTML = `
        <div class="mb-3">
            <label for="minPrice" class="form-label">Minimum Service Price</label>
            <input type="number" class="form-control" id="minPrice" required>
        </div>
        <div class="mb-3">
            <label for="maxPrice" class="form-label">Maximum Service Price</label>
            <input type="number" class="form-control" id="maxPrice" required>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="massageServices">
            <label class="form-check-label" for="massageServices">Massage Services</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="facialTreatments">
            <label class="form-check-label" for="facialTreatments">Facial Treatments</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="nailServices">
            <label class="form-check-label" for="nailServices">Nail Services</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="hairStyling">
            <label class="form-check-label" for="hairStyling">Hair Styling</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="makeupServices">
            <label class="form-check-label" for="makeupServices">Makeup Services</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="waxing">
            <label class="form-check-label" for="waxing">Waxing</label>
        </div>
    `;
            break;
        case 'Doctor':
            specificFields.innerHTML = `
        <div class="mb-3">
            <label for="specialty" class="form-label">Specialty</label>
            <input type="text" class="form-control" id="specialty" required>
        </div>
        <div class="mb-3">
            <label for="consultationFee" class="form-label">Consultation Fee</label>
            <input type="number" class="form-control" id="consultationFee" required>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="acceptsInsurance">
            <label class="form-check-label" for="acceptsInsurance">Accepts Insurance</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="emergencyServices">
            <label class="form-check-label" for="emergencyServices">Emergency Services</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="appointmentRequired">
            <label class="form-check-label" for="appointmentRequired">Appointment Required</label>
        </div>
    `;
            break;
        case 'Shopping':
            specificFields.innerHTML = `
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="clothing">
            <label class="form-check-label" for="clothing">Clothing</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="electronics">
            <label class="form-check-label" for="electronics">Electronics</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="groceries">
            <label class="form-check-label" for="groceries">Groceries</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="homeGoods">
            <label class="form-check-label" for="homeGoods">Home Goods</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="personalCare">
            <label class="form-check-label" for="personalCare">Personal Care</label>
        </div>
        <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="discountsAvailable">
            <label class="form-check-label" for="discountsAvailable">Discounts Available</label>
        </div>
    `;
            break;
    }
}

document.getElementById('backButton').addEventListener('click', function () {
    document.getElementById('businessForm').style.display = 'none';
    document.getElementById('categoryForm').style.display = 'block';
});

document.getElementById('businessForm').addEventListener('submit', function (e) {
    e.preventDefault();

    if (!validateBusinessForm()) {
        return;
    }

    // Submit form data
    const formData = new FormData();
    formData.append('title', title);
    formData.append('tagline', tagline);
    formData.append('description', description);
    formData.append('businessCategory', businessCategory);
    formData.append('website', document.getElementById('website').value);
    formData.append('phone', document.getElementById('phone').value);
    formData.append('address', document.getElementById('address').value);
    formData.append('city', document.getElementById('city').value);
    formData.append('state', document.getElementById('state').value);
    formData.append('pincode', document.getElementById('pincode').value);
    formData.append('thumbnail', document.getElementById('thumbnail').files[0]);

    const images = document.getElementById('images').files;
    for (let i = 0; i < images.length; i++) {
        formData.append('images', images[i]);
    }

    // Append category-specific fields based on businessCategory
    switch (businessCategory) {
        case 'Restaurant':
            formData.append('minPrice', document.getElementById('minPrice').value);
            formData.append('maxPrice', document.getElementById('maxPrice').value);
            formData.append('delivery', document.getElementById('delivery').checked);
            formData.append('takeOut', document.getElementById('takeOut').checked);
            formData.append('airConditioning', document.getElementById('airConditioning').checked);
            formData.append('wifi', document.getElementById('wifi').checked);
            formData.append('pureVeg', document.getElementById('pureVeg').checked);
            break;
        case 'Hotel':
            formData.append('minPrice', document.getElementById('minPrice').value);
            formData.append('maxPrice', document.getElementById('maxPrice').value);
            formData.append('roomService', document.getElementById('roomService').checked);
            formData.append('gym', document.getElementById('gym').checked);
            formData.append('pool', document.getElementById('pool').checked);
            formData.append('spa', document.getElementById('spa').checked);
            formData.append('petFriendly', document.getElementById('petFriendly').checked);
            break;
        case 'Automotive':
            formData.append('minPrice', document.getElementById('minPrice').value);
            formData.append('maxPrice', document.getElementById('maxPrice').value);
            formData.append('repairServices', document.getElementById('repairServices').checked);
            formData.append('partsSales', document.getElementById('partsSales').checked);
            formData.append('towingService', document.getElementById('towingService').checked);
            formData.append('carWash', document.getElementById('carWash').checked);
            formData.append('appointmentRequired', document.getElementById('appointmentRequired').checked);
            break;
        case 'BeautySpa':
            formData.append('minPrice', document.getElementById('minPrice').value);
            formData.append('maxPrice', document.getElementById('maxPrice').value);
            formData.append('massageServices', document.getElementById('massageServices').checked);
            formData.append('facialTreatments', document.getElementById('facialTreatments').checked);
            formData.append('nailServices', document.getElementById('nailServices').checked);
            formData.append('hairStyling', document.getElementById('hairStyling').checked);
            formData.append('makeupServices', document.getElementById('makeupServices').checked);
            formData.append('waxing', document.getElementById('waxing').checked);
            break;
        case 'Doctor':
            formData.append('specialty', document.getElementById('specialty').value);
            formData.append('consultationFee', document.getElementById('consultationFee').value);
            formData.append('acceptsInsurance', document.getElementById('acceptsInsurance').checked);
            formData.append('emergencyServices', document.getElementById('emergencyServices').checked);
            formData.append('appointmentRequired', document.getElementById('appointmentRequired').checked);
            break;
        case 'Shopping':
            formData.append('clothing', document.getElementById('clothing').checked);
            formData.append('electronics', document.getElementById('electronics').checked);
            formData.append('groceries', document.getElementById('groceries').checked);
            formData.append('homeGoods', document.getElementById('homeGoods').checked);
            formData.append('personalCare', document.getElementById('personalCare').checked);
            formData.append('discountsAvailable', document.getElementById('discountsAvailable').checked);
            break;
    }

    // Append FAQ data
    for (let i = 1; i <= faqCounter; i++) {
        const question = document.querySelector(`[name="que${i}"]`).value;
        const answer = document.querySelector(`[name="ans${i}"]`).value;
        formData.append(`faq[${i}][question]`, question);
        formData.append(`faq[${i}][answer]`, answer);
    }

    
    // Append business hours
    const businessHours = {
        monday: {
            open: document.getElementById('monAm').value,
            close: document.getElementById('monPm').value,
            openClosed: document.getElementById('inlineCheckbox1').checked
        },
        tuesday: {
            open: document.getElementById('tueAm').value,
            close: document.getElementById('tuePm').value,
            openClosed: document.getElementById('inlineCheckbox2').checked
        },
        wednesday: {
            open: document.getElementById('wedAm').value,
            close: document.getElementById('wedPm').value,
            openClosed: document.getElementById('inlineCheckbox3').checked
        },
        thursday: {
            open: document.getElementById('thuAm').value,
            close: document.getElementById('thuPm').value,
            openClosed: document.getElementById('inlineCheckbox4').checked
        },
        friday: {
            open: document.getElementById('friAm').value,
            close: document.getElementById('friPm').value,
            openClosed: document.getElementById('inlineCheckbox5').checked
        },
        saturday: {
            open: document.getElementById('satAm').value,
            close: document.getElementById('satPm').value,
            openClosed: document.getElementById('inlineCheckbox6').checked
        },
        sunday: {
            open: document.getElementById('sunAm').value,
            close: document.getElementById('sunPm').value,
            openClosed: document.getElementById('inlineCheckbox7').checked
        }
    };

    formData.append('businessHours', JSON.stringify(businessHours));

    // Submit the form data using fetch
    const totalFiles = (thumbnailFile ? 1 : 0) + imagesFiles.length;

    if (totalFiles < 5) {
        
    }
    fetch('/Listing_form/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': csrftoken,
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Business registered successfully!');
        } else {
            alert('Error registering business: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

document.getElementById('addmore').addEventListener('click', function (e) {
    e.preventDefault();
    addFAQ();
});

let faqCounter = 1;

function addFAQ() {
    faqCounter++;

    const faqContainer = document.getElementById('faqContainer');

    const faqItem = document.createElement('div');
    faqItem.className = 'faqItem';

    const questionDiv = document.createElement('div');
    questionDiv.className = 'hea';
    const questionLabel = document.createElement('b');
    questionLabel.textContent = `Question ${faqCounter}`;
    const questionTextarea = document.createElement('textarea');
    questionTextarea.type = 'text';
    questionTextarea.className = 'tat';
    questionTextarea.name = 'que' + faqCounter;
    questionTextarea.placeholder = 'Questions...';

    questionDiv.appendChild(questionLabel);
    questionDiv.appendChild(questionTextarea);

    const answerDiv = document.createElement('div');
    const answerTextarea = document.createElement('textarea');
    answerTextarea.type = 'text';
    answerTextarea.className = 'tot';
    answerTextarea.name = 'ans' + faqCounter;
    answerTextarea.placeholder = 'Answers';

    answerDiv.appendChild(answerTextarea);

    faqItem.appendChild(questionDiv);
    faqItem.appendChild(answerDiv);

    faqContainer.appendChild(faqItem);
}

const thumbnailInput = document.getElementById('thumbnail');
const imagesInput = document.getElementById('images');
const imagesContainer = document.getElementById('imagesContainer');
const submitButton = document.getElementById('businessForm').querySelector('button[type="submit"]');

const thumbnailPreview = document.getElementById('thumbnail-preview');
const imagesPreview = document.getElementById('images-preview');

thumbnailInput.addEventListener('change', checkImageCount);
imagesInput.addEventListener('change', checkImageCount);


thumbnailInput.addEventListener('change', previewThumbnail);
imagesInput.addEventListener('change', previewImages);

function checkImageCount() {
    const thumbnailFile = thumbnailInput.files[0];
    const imagesFiles = imagesInput.files;
    const totalFiles = (thumbnailFile ? 1 : 0) + imagesFiles.length;

    if (totalFiles < 5) {
        submitButton.disabled = true;
        imagesContainer.classList.add('has-danger');
    } else {
        submitButton.disabled = false;
        imagesContainer.classList.remove('has-danger');
    }
}

function validateBusinessForm() {
    const requiredFields = ['phone', 'address', 'city', 'state', 'pincode'];

    for (let i = 0; i < requiredFields.length; i++) {
        const field = document.getElementById(requiredFields[i]);
        if (!field.value) {
            alert(`Please fill out the ${field.id} field.`);
            field.focus();
            return false;
        }
    }

    return true;
}


function previewThumbnail() {    
    const file = thumbnailInput.files[0];
    const reader = new FileReader();
    reader.onload = function() {
        const img = document.createElement('img');
        img.src = reader.result;
        thumbnailPreview.appendChild(img);
    };
    reader.readAsDataURL(file);
}


function previewImages() {
    const files = imagesInput.files;
    imagesPreview.innerHTML = '';
    for (let i = 0; i < files.length; i++) {
        const file = files[i];
        const reader = new FileReader();
        reader.onload = function() {
            const img = document.createElement('img');
            img.src = reader.result;
            imagesPreview.appendChild(img);
        };
        reader.readAsDataURL(file);
    }
}