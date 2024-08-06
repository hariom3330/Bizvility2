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
    console.log(title)
    e.preventDefault();
});


document.getElementById('addmore').addEventListener('click', function(e){
    e.preventDefault();

})


const thumbnailInput = document.getElementById('thumbnail');
const imagesInput = document.getElementById('images');
const imagesContainer = document.getElementById('imagesContainer');
const submitButton = document.getElementById('businessForm').querySelector('button[type="submit"]');

thumbnailInput.addEventListener('change', checkImageCount);
imagesInput.addEventListener('change', checkImageCount);

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

checkImageCount();

const thumbnailPreview = document.getElementById('thumbnail-preview');
const imagesPreview = document.getElementById('images-preview');

thumbnailInput.addEventListener('change', previewThumbnail);
imagesInput.addEventListener('change', previewImages);

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